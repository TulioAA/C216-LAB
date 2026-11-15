from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import (
    get_db,
)

from app.schemas.maintenance import (
    ManutencaoCreate,
)

from app.services.maintenance_service import (
    criar_manutencao_service,
)

from app.services.maintenance_service import (
    listar_manutencoes_service,
)

from app.services.maintenance_service import (
    listar_manutencoes_maquina_service,
)

from app.services.maintenance_service import (
    deletar_manutencao_service,
)

from app.services.maintenance_service import (
    atualizar_manutencao_service,
)

router = APIRouter(
    prefix="/manutencoes",
    tags=["Manutenções"],
)


@router.get("/")
def listar_manutencoes(
    banco: Session = Depends(
        get_db,
    ),
):
    return listar_manutencoes_service(
        banco,
    )


@router.get(
    "/maquina/{maquina_id}"
)
def listar_por_maquina(
    maquina_id: int,
    banco: Session = Depends(
        get_db,
    ),
):
    return (
        listar_manutencoes_maquina_service(
            banco,
            maquina_id,
        )
    )


@router.post("/")
def criar_manutencao(
    manutencao: ManutencaoCreate,
    banco: Session = Depends(
        get_db,
    ),
):
    return criar_manutencao_service(
        banco,
        manutencao,
    )


@router.delete(
    "/{manutencao_id}"
)
def deletar_manutencao(
    manutencao_id: int,
    banco: Session = Depends(
        get_db,
    ),
):
    return (
        deletar_manutencao_service(
            banco,
            manutencao_id,
        )
    )


@router.put(
    "/{manutencao_id}"
)
def atualizar_manutencao(
    manutencao_id: int,
    manutencao: ManutencaoCreate,
    banco: Session = Depends(
        get_db,
    ),
):
    return (
        atualizar_manutencao_service(
            banco,
            manutencao_id,
            manutencao,
        )
    )