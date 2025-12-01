from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from services.glicemia_service import GlicemiaService

glicemia_controller = Blueprint("glicemia", __name__)

@glicemia_controller.route("/", methods=["POST"])
@jwt_required()
def create():
    user_id_raw = get_jwt_identity()
    try:
        user_id = int(user_id_raw)
    except Exception:
        return jsonify({"error": "Invalid token identity"}), 401
    data = request.json
    service = GlicemiaService()
    # accept missing data field from client and default to today
    data_date = data.get("data") if isinstance(data, dict) else None
    if not data_date:
        data_date = datetime.utcnow().strftime('%Y-%m-%d')

    record = service.create(
        user_id=user_id,
        data=data_date,
        jejum=data.get("jejum"),
        pos_prandial=data.get("pos_prandial"),
        dormir=data.get("dormir"),
        observacoes=data.get("observacoes")
    )

    return jsonify({
        "id": record.id,
        "user": record.usuario.username if getattr(record, 'usuario', None) else None,
        "data": str(record.data),
        "jejum": record.jejum,
        "pos_prandial": record.pos_prandial,
        "dormir": record.dormir,
        "observacoes": record.observacoes
    }), 201


@glicemia_controller.get('/')
@jwt_required()
def list_glicemia():
    user_id_raw = get_jwt_identity()
    try:
        user_id = int(user_id_raw)
    except Exception:
        return jsonify({"error": "Invalid token identity"}), 401

    service = GlicemiaService()
    records = service.list_by_user(user_id)

    # serialize records
    result = []
    for r in records:
        result.append({
            'id': r.id,
            'user': r.usuario.username if getattr(r, 'usuario', None) else None,
            'data': str(r.data),
            'jejum': r.jejum,
            'pos_prandial': r.pos_prandial,
            'dormir': r.dormir,
            'observacoes': r.observacoes
        })
    return jsonify(result)

@glicemia_controller.route("/<int:id>", methods=["GET"])
@jwt_required()
def get_by_id(id):
    service = GlicemiaService()
    record = service.get_by_id(id)
    if not record:
        return jsonify({"error": "Registro não encontrado"}), 404
    
    return jsonify({
        "id": record.id,
        "user": record.usuario.username if getattr(record, 'usuario', None) else None,
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
    service = GlicemiaService()
    record = service.update(
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
    service = GlicemiaService()
    if not service.delete(id):
        return jsonify({"error": "Registro não encontrado"}), 404
    return jsonify({"message": "Registro deletado"}), 200
