from config import db
from datetime import datetime

class Glicemia(db.Model):
    __tablename__ = "glicemia"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id", ondelete="CASCADE"))
    data = db.Column(db.Date, nullable=False)
    jejum = db.Column(db.Integer)
    pos_prandial = db.Column(db.Integer)
    dormir = db.Column(db.Integer)
    observacoes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    usuario = db.relationship("Usuario", back_populates="glicemia")

    def __repr__(self):
        return f"<Glicemia {self.data}>"
