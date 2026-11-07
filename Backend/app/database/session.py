from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

URL_BANCO = "sqlite:///./agromanutencao.db"

engine = create_engine(
    URL_BANCO,
    connect_args={"check_same_thread": False},
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