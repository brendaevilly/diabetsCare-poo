from config import db
from models.glicemia import Glicemia
from datetime import datetime


class GlicemiaRepository:
    """Repositório para registros de glicemia usando a instância global `db`.

    Métodos estáticos para CRUD básico alinhados com os serviços.
    """

    @staticmethod
    def create(novo: Glicemia):
        db.session.add(novo)
        db.session.commit()
        return novo

    @staticmethod
    def get_by_id(glicemia_id: int):
        return db.session.execute(db.select(Glicemia).filter_by(id=glicemia_id)).scalar_one_or_none()

    @staticmethod
    def list_by_user(usuario_id: int):
        return db.session.execute(db.select(Glicemia).filter_by(usuario_id=usuario_id)).scalars().all()

    @staticmethod
    def delete(record: Glicemia):
        db.session.delete(record)
        db.session.commit()
        return True

    @staticmethod
    def update(record: Glicemia):
        db.session.commit()
        return record
