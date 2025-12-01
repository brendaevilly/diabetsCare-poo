from config import db
from models.user import Usuario

class UserRepository:
    @staticmethod
    def get_by_username(username):
        return db.session.execute(db.select(Usuario).filter_by(username=username)).scalar_one_or_none()

    @staticmethod
    def create_user(username,password,tipo = "comum"):
        new_user = Usuario(username=username, password=password, tipo = tipo)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    @staticmethod
    def get_by_id(id):
        return db.session.execute(db.select(Usuario).filter_by(id=id)).scalar_one_or_none()

