
from repositories.user_repository import UsuarioRepository
from models.user import Usuario
from services.auth_service import AuthService
from sqlalchemy.orm import Session

class UsuarioService:
    def __init__(self):
        # Repositório e helper de autenticação
        self.repo = UsuarioRepository()
        self.auth = AuthService()

    def register(self, username: str, password: str, tipo: str = "Comum"):
        if self.repo.get_by_username(username):
            return None  # já existe
        hashed = self.auth.hash_password(password)
        novo = Usuario(username=username, password=hashed, tipo=tipo)
        return self.repo.create_user(username, hashed, tipo)
    def login(self, username: str, password: str):
        user = self.repo.get_by_username(username)
        if not user:
            return None
        if not self.auth.verify_password(user.password, password):
            return None
        token = self.auth.generate_token(user.id)
        return token

    def get_by_id(self, user_id: int):
        return self.repo.get_by_id(user_id)