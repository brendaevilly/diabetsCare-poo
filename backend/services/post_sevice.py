from repositories.post_repository import PostRepository
from models.post import Post

class PostService:
    def __init__(self):
        self.repo = PostRepository()

    def create(self, user_id, conteudo):
        post = Post(usuario_id=user_id, conteudo=conteudo)
        return self.repo.create(post)


    def list_all(self):
        return self.repo.list_all()

    def list_by_user(self, usuario_id):
        return self.repo.list_by_user(usuario_id)