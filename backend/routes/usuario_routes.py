from flask import Blueprint, request, jsonify
from models.usuario import Usuario
from database.db import db

usuario_bp = Blueprint("usuarios", __name__)


@usuario_bp.route("/usuarios", methods=["POST"])
def criar_usuario():

    data = request.get_json()

    usuario = Usuario(
        nome=data["nome"],
        email=data["email"],
        senha=data["senha"]
    )

    db.session.add(usuario)
    db.session.commit()

    return jsonify({"message": "Usuário criado"}), 201


@usuario_bp.route("/usuarios", methods=["GET"])
def listar_usuarios():

    usuarios = Usuario.query.all()

    lista = []

    for usuario in usuarios:
        lista.append({
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email
        })

    return jsonify(lista)