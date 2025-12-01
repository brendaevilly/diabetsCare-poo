# database/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .connection import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)

    alimentacoes = relationship("Alimentacao", back_populates="usuario")


class Alimentacao(Base):
    __tablename__ = "alimentacoes"

    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    alimento = Column(String, nullable=False)
    carboidratos = Column(Float, nullable=False)
    horario = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="alimentacoes")
