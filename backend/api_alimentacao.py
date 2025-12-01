from fastapi import APIRouter, Depends
from database.connection import SessionLocal
from database.dal_alimentacao import DALAlimentacao
from schemas.alimentacao import AlimentacaoCreate, AlimentacaoResponse

router = APIRouter(prefix="/alimentacao", tags=["Alimentacao"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AlimentacaoResponse)
def criar_alimentacao(data: AlimentacaoCreate, db=Depends(get_db)):
    dal = DALAlimentacao(db)
    return dal.create(data)

@router.get("/", response_model=list[AlimentacaoResponse])
def listar_alimentacao(db=Depends(get_db)):
    dal = DALAlimentacao(db)
    return dal.get_all()
