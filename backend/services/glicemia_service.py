from models.glicemia import Glicemia
from repositories.glicemia_repository import GlicemiaRepository


class GlicemiaService:
    def __init__(self):
        self.repo = GlicemiaRepository()


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


    def listar(self, db, usuario_id):
        return self.repo.list_by_user(db, usuario_id)

    def delete(self, db, glicemia_id):
        record = self.repo.get_by_id(db, glicemia_id)
        if record:
            self.repo.delete(db, record)