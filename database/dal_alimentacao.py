from sqlalchemy.orm import Session
from .models import Alimentacao

class DALAlimentacao:

    def create(self, db: Session, alimentacao: Alimentacao):
        db.add(alimentacao)
        db.commit()
        db.refresh(alimentacao)
        return alimentacao

    def get_by_id(self, db: Session, alimentacao_id: int):
        return db.query(Alimentacao).filter(Alimentacao.id == alimentacao_id).first()

    def get_by_usuario(self, db: Session, usuario_id: int):
        return db.query(Alimentacao).filter(Alimentacao.usuario_id == usuario_id).all()

    def update(self, db: Session, alimentacao_id: int, data: dict):
        alimentacao = self.get_by_id(db, alimentacao_id)
        if not alimentacao:
            return None
        for key, value in data.items():
            setattr(alimentacao, key, value)
        db.commit()
        db.refresh(alimentacao)
        return alimentacao

    def delete(self, db: Session, alimentacao_id: int):
        alimentacao = self.get_by_id(db, alimentacao_id)
        if not alimentacao:
            return False
        db.delete(alimentacao)
        db.commit()
        return True

    # CONSULTAS / RELATÓRIOS
    def get_por_dia(self, db: Session, usuario_id: int, data):
        return db.query(Alimentacao).filter(
            Alimentacao.usuario_id == usuario_id,
            Alimentacao.horario.like(f"{data}%")
        ).all()

    def carboidratos_por_dia(self, db: Session, usuario_id: int, data):
        registros = self.get_por_dia(db, usuario_id, data)
        return sum(r.carboidratos for r in registros)

    def get_intervalo(self, db: Session, usuario_id: int, inicio, fim):
        return db.query(Alimentacao).filter(
            Alimentacao.usuario_id == usuario_id,
            Alimentacao.horario >= inicio,
            Alimentacao.horario <= fim
        ).all()
