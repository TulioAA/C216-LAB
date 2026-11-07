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