import os
import sys

# Garante que o Python encontre o pacote "database"
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.connection import Base, engine
from database import models   # importa as tabelas

# Cria todas as tabelas no banco
Base.metadata.create_all(bind=engine)

print("Banco criado com sucesso!")
