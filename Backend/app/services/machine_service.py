from app.repositories.machine_repository import (
    criar_maquina,
)

from app.repositories.machine_repository import (
    listar_maquinas,
)

from app.repositories.machine_repository import (
    buscar_maquina_por_id,
)

from app.repositories.machine_repository import (
    deletar_maquina,
)

from app.repositories.machine_repository import (
    atualizar_maquina,
)


def criar_maquina_service(
    banco,
    dados_maquina,
):
    return criar_maquina(
        banco,
        dados_maquina,
    )


def listar_maquinas_service(
    banco,
):
    maquinas = listar_maquinas(
        banco,
    )

    resultado = []

    for maquina in maquinas:
        manutencao_atrasada = (
            maquina.horas_trabalhadas
            >= maquina.horas_proxima_manutencao
        )

        manutencoes = []

        for manutencao in maquina.manutencoes:
            manutencoes.append(
                {
                    "id": manutencao.id,
                    "tipo_manutencao": manutencao.tipo_manutencao,
                    "descricao": manutencao.descricao,
                    "data_manutencao": manutencao.data_manutencao,
                    "custo": manutencao.custo,
                }
            )

        resultado.append(
            {
                "id": maquina.id,
                "nome_maquina": maquina.nome_maquina,
                "marca": maquina.marca,
                "modelo": maquina.modelo,
                "ano": maquina.ano,
                "horas_trabalhadas": maquina.horas_trabalhadas,
                "horas_proxima_manutencao": maquina.horas_proxima_manutencao,
                "manutencao_atrasada": manutencao_atrasada,
                "manutencoes": manutencoes,
            }
        )

    return resultado


def buscar_maquina_service(
    banco,
    maquina_id,
):
    return buscar_maquina_por_id(
        banco,
        maquina_id,
    )


def deletar_maquina_service(
    banco,
    maquina_id,
):
    return deletar_maquina(
        banco,
        maquina_id,
    )


def atualizar_maquina_service(
    banco,
    maquina_id,
    dados_maquina,
):
    return atualizar_maquina(
        banco,
        maquina_id,
        dados_maquina,
    )