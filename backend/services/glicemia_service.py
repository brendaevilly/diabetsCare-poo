from models.glicemia import Glicemia
from repositories.glicemia_repository import GlycemiaRepository
from datetime import datetime


class GlicemiaService:
    def __init__(self):
        self.repo = GlycemiaRepository()


    def criar_registro(self, db, usuario_id, data, jejum, pos_prandial, dormir, observacoes):
        novo = Glicemia(
        usuario_id=usuario_id,
        data=data,
        jejum=jejum,
        pos_prandial=pos_prandial,
        dormir=dormir,
        observacoes=observacoes
        )
        return self.repo.create(db, novo)

    def get_by_id(self,glicemia_id):
        return self.repo.get_by_id(glicemia_id)

    def listar(self, db, usuario_id):
        return self.repo.list_by_user(db, usuario_id)

    def delete(self, db, glicemia_id):
        record = self.repo.get_by_id(db, glicemia_id)
        if record:
            self.repo.delete(db, record)

    def update(self,glicemia_id, data=None, jejum=None, pos_prandial=None, dormir=None, observacoes=None):
        record = self.repo.get_by_id(glicemia_id)
        if not record:
            return None
        if data:
            record.data = datetime.strptime(data, '%Y-%m-%d').date()
        if jejum is not None:
            record.jejum = jejum
        if pos_prandial is not None:
            record.pos_prandial = pos_prandial
        if dormir is not None:
            record.dormir = dormir
        if observacoes is not None:
            record.observacoes = observacoes
            
        return self.repo.create(record)
    