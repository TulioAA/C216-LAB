from app.repositories.machine_repository import (
    criar_maquina,
)

from app.repositories.machine_repository import (
    listar_maquinas,
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
            }
        )

    return resultado