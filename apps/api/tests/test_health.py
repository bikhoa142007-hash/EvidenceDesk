from fastapi.testclient import TestClient
from evidencedesk.main import create_app

def test_healthz_ok():
    client = TestClient(create_app())
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


