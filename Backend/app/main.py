from fastapi import FastAPI
from app.api import items

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API rodando!"}

app.include_router(items.router)
