from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database.base import Base


class Maquina(Base):
    __tablename__ = "maquinas"

    id = Column(Integer, primary_key=True)

    nome_maquina = Column(
        String,
        nullable=False,
    )

    marca = Column(
        String,
        nullable=False,
    )

    modelo = Column(
        String,
        nullable=False,
    )

    ano = Column(Integer)

    horas_trabalhadas = Column(Integer)

    horas_proxima_manutencao = Column(
        Integer
    )