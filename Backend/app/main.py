from fastapi import FastAPI
from app.api import items

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend funcionando"}
@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(items.router)
