from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.auth_service import AuthService
from repositories.user_repository import UsuarioRepository

auth_controller = Blueprint("auth", __name__)

@auth_controller.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON inválido"}), 400

    username = data.get("username")
    password = data.get("password")
    tipo = data.get("tipo", "Comum")


    user, error = AuthService.register(username, password, tipo)
    if error:
        return jsonify({"error": error}), 400

    return jsonify({
        "id": user.id,
        "username": user.username,
        "tipo": user.tipo
    }), 201


@auth_controller.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "JSON inválido"}), 400

    username = data.get("username")
    password = data.get("password")

    token = AuthService.login(username, password)
    if not token:
        return jsonify({"error": "Credenciais inválidas"}), 401

    return jsonify({"token": token})


@auth_controller.get('/me')
@jwt_required()
def me():
    user_id_raw = get_jwt_identity()
    try:
        user_id = int(user_id_raw)
    except Exception:
        return jsonify({"error": "Invalid token identity"}), 401
    if not user_id:
        return jsonify({"error": "Usuário não autenticado"}), 401
    user = UsuarioRepository.get_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify({"id": user.id, "username": user.username, "tipo": user.tipo})
