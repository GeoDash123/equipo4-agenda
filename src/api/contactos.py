from flask import Blueprint, jsonify
from src.models import Contacto



bp = Blueprint("contactos", __name__)

@bp.route("/", methods=["GET"])

def get_contacts():
    contacts = Contacto.query.all()
    return jsonify([c.to_dict() for c in contacts])