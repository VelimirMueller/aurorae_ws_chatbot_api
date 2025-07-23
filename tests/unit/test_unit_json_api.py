# tests/test_api_route.py
from tests.fixtures.json_api_blueprint_fixture import client

def test_json_api_gets_called__client_submits_valid_prompt__json_api_returns_valid_json_and_status_code_200(client, monkeypatch):
    response = client.post("/api", json={"message": "Hello"})
    assert response.status_code == 200
    assert response.is_json == True

def test_json_api_gets_called__client_submits_wrong_media_type__json_api_returns_400(client, monkeypatch):
    response = client.post("/api", data={"no-json": "no-json"}, content_type="text/plain")
    assert response.status_code == 400
    assert response.get_json() == {"error": "Content-Type must be application/json"}

def test_json_api_gets_called__get_request_received__json_api_return_405(client):
    response = client.get("/api")
    assert response.status_code == 405  # Method Not Allowed