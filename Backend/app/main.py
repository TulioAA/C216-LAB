from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Prática 4 API")
app.include_router(router)
