from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import (
    get_db,
)

from app.schemas.machine import (
    MaquinaCreate,
)

from app.services.machine_service import (
    criar_maquina_service,
)

from app.services.machine_service import (
    listar_maquinas_service,
)

from app.services.machine_service import (
    buscar_maquina_service,
)

from app.services.machine_service import (
    deletar_maquina_service,
)

from app.services.machine_service import (
    atualizar_maquina_service,
)

router = APIRouter(
    prefix="/maquinas",
    tags=["Máquinas"],
)


@router.get("/")
def listar_maquinas(
    banco: Session = Depends(
        get_db,
    ),
):
    return listar_maquinas_service(
        banco,
    )


@router.get("/{maquina_id}")
def buscar_maquina(
    maquina_id: int,
    banco: Session = Depends(
        get_db,
    ),
):
    return buscar_maquina_service(
        banco,
        maquina_id,
    )


@router.post("/")
def criar_maquina(
    maquina: MaquinaCreate,
    banco: Session = Depends(
        get_db,
    ),
):
    return criar_maquina_service(
        banco,
        maquina,
    )


@router.delete("/{maquina_id}")
def deletar_maquina(
    maquina_id: int,
    banco: Session = Depends(
        get_db,
    ),
):
    return deletar_maquina_service(
        banco,
        maquina_id,
    )


@router.put(
    "/{maquina_id}"
)
def atualizar_maquina(
    maquina_id: int,
    maquina: MaquinaCreate,
    banco: Session = Depends(
        get_db,
    ),
):
    return atualizar_maquina_service(
        banco,
        maquina_id,
        maquina,
    )