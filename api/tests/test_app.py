import app as app_module


def test_healthz_returns_ok():
    client = app_module.app.test_client()
    resp = client.get("/healthz")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_version_returns_app_version(monkeypatch):
    monkeypatch.setattr(app_module, "APP_VERSION", "sha-abc1234")
    client = app_module.app.test_client()
    resp = client.get("/version")
    assert resp.get_json() == {"version": "sha-abc1234"}


def test_add_item_without_name_returns_400():
    client = app_module.app.test_client()
    resp = client.post("/items", json={})
    assert resp.status_code == 400
