from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.glicemia_service import GlicemiaService

glicemia_controller = Blueprint("glicemia", __name__)

@glicemia_controller.route("/", methods=["POST"])
@jwt_required()
def create():
    user_id = get_jwt_identity()
    data = request.json

    record = GlicemiaService.create(
        user_id=user_id,
        data=data["data"],
        jejum=data.get("jejum"),
        pos_prandial=data.get("pos_prandial"),
        dormir=data.get("dormir"),
        observacoes=data.get("observacoes")
    )

    return jsonify({"id": record.id}), 201

@glicemia_controller.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_by_id(id):
    record = GlicemiaService.get_by_id(id)
    if not record:
        return jsonify({"error": "Registro não encontrado"}), 404
    
    return jsonify({
        "id": record.id,
        "data": str(record.data),
        "jejum": record.jejum,
        "pos_prandial": record.pos_prandial,
        "dormir": record.dormir,
        "observacoes": record.observacoes
    })


@glicemia_controller.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update(id):
    data = request.json
    record = GlicemiaService.update(
        glicemia_id=id,
        data=data.get("data"),
        jejum=data.get("jejum"),
        pos_prandial=data.get("pos_prandial"),
        dormir=data.get("dormir"),
        observacoes=data.get("observacoes")
    )
    if not record:
        return jsonify({"error": "Registro não encontrado"}), 404
    
    return jsonify({"message": "Registro atualizado com sucesso"}), 200


@glicemia_controller.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    if not GlicemiaService.delete(id):
        return jsonify({"error": "Registro não encontrado"}), 404
    return jsonify({"message": "Registro deletado"}), 200
