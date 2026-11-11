from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.machines import (
    router as maquinas_router,
)

from app.api.maintenances import (
    router as manutencoes_router,
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(maquinas_router)

app.include_router(manutencoes_router)


@app.get("/")
def root():
    return {
        "mensagem": "API AgroManutencao"
    }