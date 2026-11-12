import os

import psycopg
from flask import Flask, jsonify, request

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "unknown")
DATABASE_URL = os.environ.get("DATABASE_URL", "")


def get_conn():
    return psycopg.connect(DATABASE_URL, connect_timeout=3)


@app.get("/healthz")
def healthz():
    return jsonify(status="ok")


@app.get("/readyz")
def readyz():
    try:
        with get_conn() as conn:
            conn.execute("SELECT 1")
        return jsonify(status="ready")
    except psycopg.Error  as exc:
        return jsonify(status="not ready", error=str(exc)), 503


@app.get("/version")
def version():
    return jsonify(version=APP_VERSION)


@app.get("/items")
def list_items():
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT id, name, created_at FROM items ORDER BY id"
        ).fetchall()
    return jsonify(
        [{"id": r[0], "name": r[1], "created_at": r[2].isoformat()} for r in rows]
    )


@app.post("/items")
def add_item():
    name = (request.get_json(silent=True) or {}).get("name")
    if not name:
        return jsonify(error="name is required"), 400
    with get_conn() as conn:
        row = conn.execute(
            "INSERT INTO items (name) VALUES (%s) RETURNING id", (name,)
        ).fetchone()
    return jsonify(id=row[0], name=name), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
