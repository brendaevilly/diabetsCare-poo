from config import db
from models.post import Post

class PostRepository:
    def create(post):
        db.session.add(post)
        db.session.commit()
        return post

    def list_all():
        return Post.query.order_by(Post.timestamp.desc()).all()
