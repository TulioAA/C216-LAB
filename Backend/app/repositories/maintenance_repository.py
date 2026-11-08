from app.models.maintenance import (
    Manutencao,
)


def criar_manutencao(
    banco,
    dados_manutencao,
):
    manutencao = Manutencao(
        **dados_manutencao.model_dump()
    )

    banco.add(manutencao)

    banco.commit()

    banco.refresh(manutencao)

    return manutencao


def listar_manutencoes(
    banco,
):
    return banco.query(
        Manutencao
    ).all()


def listar_manutencoes_por_maquina(
    banco,
    maquina_id,
):
    return (
        banco.query(
            Manutencao
        )
        .filter(
            Manutencao.maquina_id
            == maquina_id
        )
        .all()
    )


def buscar_manutencao_por_id(
    banco,
    manutencao_id,
):
    return (
        banco.query(
            Manutencao
        )
        .filter(
            Manutencao.id
            == manutencao_id
        )
        .first()
    )


def deletar_manutencao(
    banco,
    manutencao_id,
):
    manutencao = (
        buscar_manutencao_por_id(
            banco,
            manutencao_id,
        )
    )

    if manutencao:
        banco.delete(
            manutencao
        )

        banco.commit()

    return manutencao


def atualizar_manutencao(
    banco,
    manutencao_id,
    dados_manutencao,
):
    manutencao = (
        buscar_manutencao_por_id(
            banco,
            manutencao_id,
        )
    )

    if not manutencao:
        return None

    manutencao.maquina_id = (
        dados_manutencao.maquina_id
    )

    manutencao.tipo_manutencao = (
        dados_manutencao.tipo_manutencao
    )

    manutencao.descricao = (
        dados_manutencao.descricao
    )

    manutencao.data_manutencao = (
        dados_manutencao.data_manutencao
    )

    manutencao.custo = (
        dados_manutencao.custo
    )

    banco.commit()

    banco.refresh(
        manutencao
    )

    return manutencao