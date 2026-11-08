from fastapi import FastAPI

from app.api.machines import (
    router as maquinas_router,
)

from app.api.maintenances import (
    router as manutencoes_router,
)

from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(maquinas_router)

app.include_router(manutencoes_router)


@app.get("/")
def root():
    return {
        "mensagem": "API AgroManutencao"
    }