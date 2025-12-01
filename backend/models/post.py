from config import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id", ondelete="CASCADE"))
    conteudo = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    usuario = db.relationship("Usuario", back_populates="posts")

    def __repr__(self):
        return f"<Post {self.id}>"
