import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Backend funcionando"}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@pytest.mark.parametrize("endpoint,expected", [
    ("/", {"message": "Backend funcionando"}),
    ("/health", {"status": "ok"}),
])
def test_parametrizado(endpoint, expected):
    response = client.get(endpoint)
    assert response.json() == expected

@pytest.fixture
def custom_client():
    return TestClient(app)

def test_fixture_client(custom_client):
    response = custom_client.get("/health")
    assert response.status_code == 200

def test_endpoint_invalido():
    response = client.get("/naoexiste")
    assert response.status_code == 404
