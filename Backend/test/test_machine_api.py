from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_listar_maquinas():
    response = client.get("/maquinas/")

    assert response.status_code == 200