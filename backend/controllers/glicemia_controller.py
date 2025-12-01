from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.glicemia_service import GlicemiaService

glicemia_controller = Blueprint("glicemia", __name__)

@glicemia_controller.post("/")
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


@glicemia_controller.get("/")
@jwt_required()
def list_all():
    user_id = get_jwt_identity()

    records = GlicemiaService.list_by_user(user_id)

    return jsonify([
        {
            "id": r.id,
            "data": str(r.data),
            "jejum": r.jejum,
            "pos_prandial": r.pos_prandial,
            "dormir": r.dormir,
            "observacoes": r.observacoes
        } for r in records
    ])


@glicemia_controller.delete("/<int:id>")
@jwt_required()
def delete(id):
    GlicemiaService.delete(id)
    return jsonify({"message": "Registro deletado"})
