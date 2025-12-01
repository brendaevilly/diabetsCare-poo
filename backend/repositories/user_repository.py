from config import db
from models.user import Usuario

class UserRepository:
    def find_by_username(username):
        return Usuario.query.filter_by(username=username).first()

   
    def create(user):
        db.session.add(user)
        db.session.commit()
        return user

 
    def get_by_id(user_id):
        return Usuario.query.get(user_id)
