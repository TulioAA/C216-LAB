import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.api import routes

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_items():
    routes.items.clear()

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Backend funcionando"

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_list_items_empty():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []

def test_create_item_success():
    response = client.post("/items", json={"name": "Item 1", "description": "Teste"})
    assert response.status_code == 200
    assert response.json()["name"] == "Item 1"

def test_create_item_missing_name():
    response = client.post("/items", json={"description": "sem nome"})
    assert response.status_code == 422

def test_get_item_success():
    client.post("/items", json={"name": "Item 2"})
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Item 2"

def test_get_item_not_found():
    response = client.get("/items/999")
    assert response.status_code == 200
    assert response.json()["error"] == "Item not found"

def test_update_item_success():
    client.post("/items", json={"name": "Item 3"})
    response = client.put("/items/1", json={"name": "Item 3 atualizado"})
    assert response.status_code == 200
    assert response.json()["name"] == "Item 3 atualizado"

def test_patch_item_success():
    client.post("/items", json={"name": "Item 4"})
    response = client.patch("/items/1", json={"description": "Nova descrição"})
    assert response.status_code == 200
    assert response.json()["description"] == "Nova descrição"

def test_patch_item_not_found():
    response = client.patch("/items/999", json={"description": "Nada"})
    assert response.status_code == 200
    assert response.json()["error"] == "Item not found"

def test_delete_item_success():
    client.post("/items", json={"name": "Item 5"})
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert "error" not in response.json()

def test_delete_item_not_found():
    response = client.delete("/items/999")
    assert response.status_code == 200
    assert response.json()["error"] == "Item not found"
