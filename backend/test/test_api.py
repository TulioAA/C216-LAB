from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "mensagem": "API AgroManutencao"
    }


def test_listar_maquinas():
    response = client.get("/maquinas/")

    assert response.status_code == 200


def test_listar_manutencoes():
    response = client.get("/manutencoes/")

    assert response.status_code == 200