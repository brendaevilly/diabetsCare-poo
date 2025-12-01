from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from repositories.user_repository import UsuarioRepository
from models.user import Usuario

class AuthService:

    def hash_password(self, password: str) -> str:
            return generate_password_hash(password)

    def verify_password(self, hashed_password: str, password: str) -> bool:
            return check_password_hash(hashed_password, password)

    def generate_token(self, user_id: int) -> str:
            return create_access_token(identity=str(user_id))
    @staticmethod
    def register(username, password, tipo="Comum"):
        if UsuarioRepository.get_by_username(username):
            return None, "Usuário já existe"

        hashed = generate_password_hash(password)   # gera hash da senha
        user = UsuarioRepository.create_user(username, hashed, tipo)  # passa o hash
        return user, None

    @staticmethod
    def login(username, password):
        user = UsuarioRepository.get_by_username(username)
        if not user or not check_password_hash(user.password, password):
            return None
        # ensure token identity is a string (some PyJWT validators require subject to be string)
        token = create_access_token(identity=str(user.id))
        return token
