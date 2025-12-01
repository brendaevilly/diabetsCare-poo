# database/dal.py
from .connection import SessionLocal
from .models import Alimentacao

class AlimentacaoDAL:

    def __init__(self):
        self.session = SessionLocal()

    def adicionar(self, usuario_id, alimento, carboidratos):
        nova = Alimentacao(
            usuario_id=usuario_id,
            alimento=alimento,
            carboidratos=carboidratos
        )
        self.session.add(nova)
        self.session.commit()
        return nova

    def listar_por_usuario(self, usuario_id):
        return (
            self.session.query(Alimentacao)
            .filter(Alimentacao.usuario_id == usuario_id)
            .order_by(Alimentacao.horario.desc())
            .all()
        )

    def relatorio_total_carboidratos(self, usuario_id):
        resultado = (
            self.session.query(Alimentacao)
            .filter(Alimentacao.usuario_id == usuario_id)
            .all()
        )
        return sum(item.carboidratos for item in resultado)
