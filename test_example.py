from fastapi.testclient import TestClient
from example import app

test_agent = TestClient(app)

def test_path():
    res = test_agent.get("/items/42")
    assert res.status_code == 200
    assert res.json() == {"fetch": "Fetched 1 of 42"}
    

def test_get_path_query():
    r = test_agent.get("/items/42?count=5")
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 5 of 42"}


def test_get_malformed():
    r = test_agent.get("/items")
    assert r.status_code != 200