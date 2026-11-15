from pydantic import BaseModel


class ManutencaoCreate(BaseModel):
    maquina_id: int
    tipo_manutencao: str
    descricao: str
    data_manutencao: str
    custo: int


class ManutencaoResponse(
    ManutencaoCreate
):
    id: int

    class Config:
        from_attributes = True