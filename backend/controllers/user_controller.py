from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.usuario_service import UserService

user_controller = Blueprint("user", __name__)

@user_controller.get("/me")
@jwt_required()
def get_me():
    user_id = get_jwt_identity()
    user = UserService().get_by_id(user_id)

    return jsonify({
        "id": user.id,
        "username": user.username,
        "tipo": user.tipo
    })
