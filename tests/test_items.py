import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_create_and_get_item():
    payload = {"id": 1, "name": "Widget", "description": "A test widget"}
    r = client.post("/api/v1/items/", json=payload)
    assert r.status_code == 201
    r2 = client.get("/api/v1/items/1")
    assert r2.json()["name"] == "Widget"
