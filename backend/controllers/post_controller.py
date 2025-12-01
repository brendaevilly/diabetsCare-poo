from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.post_sevice import PostService

post_controller = Blueprint("post", __name__)

@post_controller.route("/", methods=["POST"])
@jwt_required()
def create_post():
    user_id_raw = get_jwt_identity()
    try:
        user_id = int(user_id_raw)
    except Exception:
        return jsonify({"error": "Invalid token identity"}), 401
    data = request.json

    service = PostService()
    post = service.create(user_id, data["conteudo"])

    return jsonify({
        "id": post.id,
        "user": post.usuario.username if getattr(post, 'usuario', None) else None,
        "content": post.conteudo,
        "timestamp": str(post.timestamp)
    }), 201


@post_controller.get("/")
def list_posts():
    service = PostService()
    posts = service.list_all()

    return jsonify([
        {
            "id": p.id,
            "user": p.usuario.username if getattr(p, 'usuario', None) else None,
            "content": p.conteudo,
            "timestamp": str(p.timestamp)
        }
        for p in posts
    ])


@post_controller.get('/user/<int:user_id>')
def list_posts_by_user(user_id: int):
    service = PostService()
    posts = service.list_by_user(user_id)
    return jsonify([
        {
            "id": p.id,
            "user": p.usuario.username if getattr(p, 'usuario', None) else None,
            "content": p.conteudo,
            "timestamp": str(p.timestamp)
        }
        for p in posts
    ])
