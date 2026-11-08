from app.repositories.maintenance_repository import (
    criar_manutencao,
)

from app.repositories.maintenance_repository import (
    listar_manutencoes,
)

from app.repositories.maintenance_repository import (
    listar_manutencoes_por_maquina,
)

from app.repositories.maintenance_repository import (
    deletar_manutencao,
)

from app.repositories.maintenance_repository import (
    atualizar_manutencao,
)


def criar_manutencao_service(
    banco,
    dados_manutencao,
):
    return criar_manutencao(
        banco,
        dados_manutencao,
    )


def listar_manutencoes_service(
    banco,
):
    return listar_manutencoes(
        banco,
    )


def listar_manutencoes_maquina_service(
    banco,
    maquina_id,
):
    return listar_manutencoes_por_maquina(
        banco,
        maquina_id,
    )


def deletar_manutencao_service(
    banco,
    manutencao_id,
):
    return deletar_manutencao(
        banco,
        manutencao_id,
    )


def atualizar_manutencao_service(
    banco,
    manutencao_id,
    dados_manutencao,
):
    return atualizar_manutencao(
        banco,
        manutencao_id,
        dados_manutencao,
    )