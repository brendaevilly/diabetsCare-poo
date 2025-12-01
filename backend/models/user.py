from config import db
from datetime import datetime

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    tipo = db.Column(db.String(50), default="Comum")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    glicemia = db.relationship("Glicemia", back_populates="usuario", cascade="all, delete")
    posts = db.relationship("Post", back_populates="usuario", cascade="all, delete")

    def __repr__(self):
        return f"<Usuario {self.username}>"
