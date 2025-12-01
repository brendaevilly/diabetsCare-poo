from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from database.dal_alimentacao import DALAlimentacao
from schemas.alimentacao import AlimentacaoCreate, AlimentacaoResponse
from database.models import Alimentacao

router = APIRouter(prefix="/alimentacao", tags=["Alimentação"])
dal = DALAlimentacao()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AlimentacaoResponse)
def criar_alimentacao(data: AlimentacaoCreate, db: Session = Depends(get_db)):
    nova = Alimentacao(**data.dict())
    return dal.create(db, nova)

@router.get("/{id}", response_model=AlimentacaoResponse)
def buscar_por_id(id: int, db: Session = Depends(get_db)):
    return dal.get_by_id(db, id)

@router.get("/usuario/{usuario_id}")
def listar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    return dal.get_by_usuario(db, usuario_id)

@router.put("/{id}")
def atualizar(id: int, data: dict, db: Session = Depends(get_db)):
    return dal.update(db, id, data)

@router.delete("/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    return dal.delete(db, id)


@router.get("/relatorio/dia/{usuario_id}/{data}")
def relatorio_dia(usuario_id: int, data: str, db: Session = Depends(get_db)):
    return {
        "total_carboidratos": dal.carboidratos_por_dia(db, usuario_id, data),
        "registros": dal.get_por_dia(db, usuario_id, data)
    }

@router.get("/relatorio/intervalo/{usuario_id}")
def relatorio_intervalo(usuario_id: int, inicio: str, fim: str, db: Session = Depends(get_db)):
    return dal.get_intervalo(db, usuario_id, inicio, fim)
