from models.glicemia import Glicemia
from repositories.glicemia_repository import GlicemiaRepository
from datetime import datetime


class GlicemiaService:
    def __init__(self):
        self.repo = GlicemiaRepository()


    def create(self, usuario_id=None, user_id=None, data=None, jejum=None, pos_prandial=None, dormir=None, observacoes=None):
        # accept either `usuario_id` or `user_id` keywords (controllers sometimes use user_id)
        if usuario_id is None:
            usuario_id = user_id
        # normalize date: allow 'data' as str yyyy-mm-dd or a date object
        if isinstance(data, str):
            try:
                data = datetime.strptime(data, '%Y-%m-%d').date()
            except ValueError:
                # leave as-is and let SQLAlchemy/types raise or handle it
                pass

        novo = Glicemia(
            usuario_id=usuario_id,
            data=data,
            jejum=jejum,
            pos_prandial=pos_prandial,
            dormir=dormir,
            observacoes=observacoes
        )
        return self.repo.create(novo)

    def get_by_id(self, glicemia_id):
        return self.repo.get_by_id(glicemia_id)

    def list_by_user(self, usuario_id):
        return self.repo.list_by_user(usuario_id)

    def delete(self, glicemia_id):
        record = self.repo.get_by_id(glicemia_id)
        if record:
            return self.repo.delete(record)
        return False

    def update(self, glicemia_id, data=None, jejum=None, pos_prandial=None, dormir=None, observacoes=None):
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

        return self.repo.update(record)
    