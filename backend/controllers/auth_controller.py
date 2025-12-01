from flask import Blueprint, request, jsonify
from services.auth_service import AuthService

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
    return jsonify({"message": "Usuário criado com sucesso"}), 201


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
