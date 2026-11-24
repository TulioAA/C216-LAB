from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_buscar_maquina():
    response = client.get("/maquinas/1")

    assert response.status_code in [200, 404]


def test_criar_maquina():
    response = client.post(
        "/maquinas/",
        json={
            "nome_maquina": "Teste",
            "marca": "John Deere",
            "modelo": "6110J",
            "ano": 2024,
            "horas_trabalhadas": 100,
            "horas_proxima_manutencao": 500,
        },
    )

    assert response.status_code in [200, 201]


def test_atualizar_maquina():
    response = client.put(
        "/maquinas/1",
        json={
            "nome_maquina": "Atualizada",
            "marca": "John Deere",
            "modelo": "6110J",
            "ano": 2024,
            "horas_trabalhadas": 150,
            "horas_proxima_manutencao": 600,
        },
    )

    assert response.status_code in [200, 404]


def test_deletar_maquina():
    response = client.delete("/maquinas/1")

    assert response.status_code in [200, 404]


def test_listar_manutencao_por_maquina():
    response = client.get("/manutencoes/maquina/1")

    assert response.status_code == 200


def test_atualizar_manutencao():
    response = client.put(
        "/manutencoes/1",
        json={
            "maquina_id": 1,
            "tipo_manutencao": "Corretiva",
            "descricao": "Atualizada",
            "data_manutencao": "2026-11-14",
            "custo": 500,
        },
    )

    assert response.status_code in [200, 404]


def test_deletar_manutencao():
    response = client.delete("/manutencoes/1")

    assert response.status_code in [200, 404]