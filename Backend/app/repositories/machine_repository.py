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