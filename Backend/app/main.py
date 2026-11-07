from fastapi import FastAPI

from app.api.machines import router
from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(
    bind=engine
)

app = FastAPI()

app.include_router(router)


@app.get("/")
def root():
    return {
        "mensagem": "API AgroManutencao"
    }