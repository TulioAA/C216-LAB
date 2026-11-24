from app.services.machine_service import (
    verificar_manutencao_atrasada
)


def test_manutencao_atrasada():
    assert verificar_manutencao_atrasada(
        horas_trabalhadas=5000,
        horas_proxima_manutencao=4000,
    ) is True


def test_manutencao_em_dia():
    assert verificar_manutencao_atrasada(
        horas_trabalhadas=3000,
        horas_proxima_manutencao=4000,
    ) is False


def test_manutencao_no_limite():
    assert verificar_manutencao_atrasada(
        horas_trabalhadas=4000,
        horas_proxima_manutencao=4000,
    ) is True

def test_manutencao_zero_horas():
    assert verificar_manutencao_atrasada(
        horas_trabalhadas=0,
        horas_proxima_manutencao=100,
    ) is False


def test_manutencao_grande():
    assert verificar_manutencao_atrasada(
        horas_trabalhadas=10000,
        horas_proxima_manutencao=100,
    ) is True