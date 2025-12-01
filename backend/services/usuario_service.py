
from repositories.user_repository import UsuarioRepository
from models.user import Usuario
from services.auth_service import AuthService
from sqlalchemy.orm import Session

class UsuarioService:
    def __init__(self):
        self.repo = UsuarioRepository()
        self.auth = AuthService()

    def register(self, db: Session, username: str, password: str, tipo: str = "Comum"):
        if self.repo.get_by_username(db, username):
            return None  # já existe
        hashed = self.auth.hash_password(password)
        novo = Usuario(username=username, password=hashed, tipo=tipo)
        return self.repo.create(db, novo)

    def login(self, db: Session, username: str, password: str):
        user = self.repo.get_by_username(db, username)
        if not user:
            return None
        if not self.auth.verify_password(user.password, password):
            return None
        token = self.auth.generate_token(user.id)
        return token

    def get_by_id(self, db: Session, user_id: int):
        return self.repo.get_by_id(db, user_id)
