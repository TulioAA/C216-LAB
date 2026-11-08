from app.models.machine import Maquina


def criar_maquina(
    banco,
    dados_maquina,
):
    maquina = Maquina(
        **dados_maquina.model_dump()
    )

    banco.add(maquina)
    banco.commit()
    banco.refresh(maquina)

    return maquina


def listar_maquinas(
    banco,
):
    return banco.query(
        Maquina
    ).all()


def buscar_maquina_por_id(
    banco,
    maquina_id,
):
    return (
        banco.query(Maquina)
        .filter(
            Maquina.id == maquina_id
        )
        .first()
    )


def deletar_maquina(
    banco,
    maquina_id,
):
    maquina = buscar_maquina_por_id(
        banco,
        maquina_id,
    )

    if maquina:
        banco.delete(maquina)
        banco.commit()

    return maquina


def atualizar_maquina(
    banco,
    maquina_id,
    dados_maquina,
):
    maquina = buscar_maquina_por_id(
        banco,
        maquina_id,
    )

    if not maquina:
        return None

    maquina.nome_maquina = (
        dados_maquina.nome_maquina
    )

    maquina.marca = (
        dados_maquina.marca
    )

    maquina.modelo = (
        dados_maquina.modelo
    )

    maquina.ano = (
        dados_maquina.ano
    )

    maquina.horas_trabalhadas = (
        dados_maquina.horas_trabalhadas
    )

    maquina.horas_proxima_manutencao = (
        dados_maquina.horas_proxima_manutencao
    )

    banco.commit()

    banco.refresh(maquina)

    return maquina