import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "unknown")


@app.get("/healthz")
def healthz():
    return jsonify(status="ok")


@app.get("/version")
def version():
    return jsonify(version=APP_VERSION)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)



