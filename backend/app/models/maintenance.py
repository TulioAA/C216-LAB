from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import relationship

from app.database.base import Base


class Manutencao(Base):
    __tablename__ = "manutencoes"

    id = Column(
        Integer,
        primary_key=True,
    )

    maquina_id = Column(
        Integer,
        ForeignKey("maquinas.id"),
        nullable=False,
    )

    tipo_manutencao = Column(
        String,
        nullable=False,
    )

    descricao = Column(
        String,
        nullable=False,
    )

    data_manutencao = Column(
        String,
        nullable=False,
    )

    custo = Column(
        Integer,
        nullable=False,
    )

    maquina = relationship(
        "Maquina",
        back_populates="manutencoes",
    )