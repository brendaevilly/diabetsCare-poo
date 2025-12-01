from pydantic import BaseModel
from datetime import datetime

class AlimentacaoBase(BaseModel):
    usuario_id: int
    alimento: str
    carboidratos: float
    horario: datetime

class AlimentacaoCreate(AlimentacaoBase):
    pass

class AlimentacaoUpdate(BaseModel):
    alimento: str | None = None
    carboidratos: float | None = None
    horario: datetime | None = None

class AlimentacaoOut(AlimentacaoBase):
    id: int

    class Config:
        orm_mode = True
