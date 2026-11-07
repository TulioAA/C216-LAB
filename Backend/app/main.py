import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import items

app = FastAPI()

# CORS
cors_origins = os.getenv(
    "CORS_ORIGINS",
    "http://localhost:5173",
)

origins = [
    origin.strip()
    for origin in cors_origins.split(",")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend funcionando"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(items.router)