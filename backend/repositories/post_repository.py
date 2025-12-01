from config import db
from models.post import Post


class PostRepository:
    """Repositório para posts usando `db` global."""

    @staticmethod
    def create(post: Post):
        db.session.add(post)
        db.session.commit()
        return post

    @staticmethod
    def list_all():
        return Post.query.order_by(Post.timestamp.desc()).all()

    @staticmethod
    def list_by_user(usuario_id: int):
        return Post.query.filter_by(usuario_id=usuario_id).order_by(Post.timestamp.desc()).all()
