import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@db:5432/agromanutencao",
)

engine = create_engine(
    DATABASE_URL
)

SessaoLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    banco = SessaoLocal()

    try:
        yield banco
    finally:
        banco.close()