from config import db
from models.glicemia import Glicemia

class GlicemiaRepository:
    def create(record):
        db.session.add(record)
        db.session.commit()
        return record

    def get_all_by_user(user_id):
        return Glicemia.query.filter_by(usuario_id=user_id).all()

    def get_by_id(glicemia_id):
        return Glicemia.query.get(glicemia_id)

    def delete(record):
        db.session.delete(record)
        db.session.commit()
        return True