from pydantic import BaseModel


class MaquinaCreate(BaseModel):
    nome_maquina: str
    marca: str
    modelo: str
    ano: int
    horas_trabalhadas: int
    horas_proxima_manutencao: int


class MaquinaResponse(
    MaquinaCreate
):
    id: int

    class Config:
        from_attributes = True