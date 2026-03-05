from flask import Blueprint, request, jsonify
from models.chamado import Chamado
from database.db import db

chamado_bp = Blueprint("chamados", __name__)


@chamado_bp.route("/chamados", methods=["GET"])
def listar_chamados():

    chamados = Chamado.query.all()

    lista = []

    for chamado in chamados:
        lista.append({
            "id": chamado.id,
            "titulo": chamado.titulo,
            "descricao": chamado.descricao,
            "status": chamado.status
        })

    return jsonify(lista)


@chamado_bp.route("/chamados", methods=["POST"])
def criar_chamado():

    data = request.get_json()

    titulo = data.get("titulo")
    descricao = data.get("descricao")

    if not titulo or not descricao:
        return jsonify({"erro": "titulo e descricao são obrigatórios"}), 400

    chamado = Chamado(
        titulo=titulo,
        descricao=descricao,
        status="aberto"
    )

    db.session.add(chamado)
    db.session.commit()

    return jsonify({"message": "Chamado criado"}), 201


@chamado_bp.route("/chamados/<int:id>", methods=["PUT"])
def atualizar_chamado(id):

    chamado = Chamado.query.get(id)

    if not chamado:
        return jsonify({"erro": "Chamado não encontrado"}), 404

    data = request.get_json()

    chamado.status = data.get("status", chamado.status)

    db.session.commit()

    return jsonify({"message": "Chamado atualizado"})


@chamado_bp.route("/chamados/<int:id>", methods=["DELETE"])
def deletar_chamado(id):

    chamado = Chamado.query.get(id)

    if not chamado:
        return jsonify({"erro": "Chamado não encontrado"}), 404

    db.session.delete(chamado)
    db.session.commit()

    return jsonify({"message": "Chamado deletado"})


