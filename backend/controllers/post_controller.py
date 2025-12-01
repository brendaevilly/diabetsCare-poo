from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.post_sevice import PostService

post_controller = Blueprint("post", __name__)

@post_controller.post("/")
@jwt_required()
def create_post():
    user_id = get_jwt_identity()
    data = request.json

    post = PostService.create(user_id, data["conteudo"])

    return jsonify({"id": post.id}), 201


@post_controller.get("/")
def list_posts():
    posts = PostService.list_all()

    return jsonify([
        {
            "id": p.id,
            "usuario_id": p.usuario_id,
            "conteudo": p.conteudo,
            "timestamp": str(p.timestamp)
        }
        for p in posts
    ])
