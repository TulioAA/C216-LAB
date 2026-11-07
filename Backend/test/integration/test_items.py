from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_list_items():
    # cria um item
    response = client.post("/items/", json={"name": "Teste", "description": "Desc"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Teste"
    assert data["description"] == "Desc"
    assert "id" in data

    # lista os itens e verifica se o criado aparece
    response = client.get("/items/")
    assert response.status_code == 200
    items = response.json()
    assert any(i["name"] == "Teste" for i in items)
