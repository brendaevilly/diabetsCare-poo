from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from repositories.user_repository import UserRepository
from models.user import Usuario

class AuthService:

    @staticmethod
    def register(username, password, tipo="Comum"):
        if UserRepository.get_by_username(username):
            return None, "Usuário já existe"

        hashed = generate_password_hash(password)   # gera hash da senha
        user = UserRepository.create_user(username, hashed, tipo)  # passa o hash
        return user, None

    @staticmethod
    def login(username, password):
        user = UserRepository.get_by_username(username)
        if not user or not check_password_hash(user.password, password):
            return None
        token = create_access_token(identity=user.id)
        return token
