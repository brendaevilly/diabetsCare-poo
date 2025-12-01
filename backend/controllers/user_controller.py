from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.usuario_service import UsuarioService

user_controller = Blueprint("user", __name__)

@user_controller.get("/me")
@jwt_required()
def get_me():
    user_id_raw = get_jwt_identity()
    try:
        user_id = int(user_id_raw)
    except Exception:
        return jsonify({"error": "Invalid token identity"}), 401
    user = UsuarioService().get_by_id(user_id)

    return jsonify({
        "id": user.id,
        "username": user.username,
        "tipo": user.tipo
    })
