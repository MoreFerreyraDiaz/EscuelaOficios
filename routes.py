from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from . import db
from .models import Contacto
from .schemas import ContactoCreateSchema

contacto_bp = Blueprint('contacto_bp', __name__)

@contacto_bp.route("/api/contacto", methods=["POST"])
def guardar_contacto():
    try:
        datos = ContactoCreateSchema(**request.get_json())
    except ValidationError as e:
        return jsonify({'errors': e.errors()}), 400

    # Crear y guardar el nuevo contacto
    nuevo = Contacto(**datos.model_dump())
    db.session.add(nuevo)
    db.session.commit()

    return jsonify({'mensaje': 'Contacto guardado con éxito'}), 201

