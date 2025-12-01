import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

# Usar a variável DATABASE_URL definida no docker-compose
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://diabetscare_user:diabetscare_pass@postgres:5432/diabetscare_db"
)

SECRET_KEY = os.getenv("SECRET_KEY", "chavesecreta")
JWT_SECRET = os.getenv("JWT_SECRET", SECRET_KEY)
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXP_SECONDS = int(os.getenv("JWT_EXP_SECONDS", 60 * 60 * 24))  # 1 dia padrão

# Criar instância do SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    """
    Inicializa o banco de dados com a aplicação Flask.
    Esta função deve ser chamada no app.py após criar a instância do Flask.
    """
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = SECRET_KEY
    
    # Inicializa o SQLAlchemy com a aplicação
    db.init_app(app)
    
    # Cria as tabelas (se ainda não existirem)
    with app.app_context():
        db.create_all()