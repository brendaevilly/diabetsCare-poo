from pydantic import BaseModel
from datetime import datetime

class AlimentacaoBase(BaseModel):
    usuario_id: int
    descricao: str
    carboidratos: float
    horario: datetime

class AlimentacaoCreate(AlimentacaoBase):
    pass

class AlimentacaoUpdate(BaseModel):
    descricao: str | None = None
    carboidratos: float | None = None
    horario: datetime | None = None

class AlimentacaoResponse(AlimentacaoBase):
    id: int

    class Config:
        orm_mode = True
