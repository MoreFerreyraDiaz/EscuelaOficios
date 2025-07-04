from . import crear_app
from python.models import Contacto
from flask import request, jsonify
from flask_cors import CORS
from python.models import db, Contacto
import re


app = crear_app()
CORS(app)

with app.app_context():
    db.create_all()

db.init_app(app)


# Validaciones
EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
PHONE_REGEX = re.compile(r"^\d{8,15}$")

# /api/contacto
@app.route('/api/contacto', methods=['POST'])
def contacto():
    data = request.get_json()

    nombre = data.get('nombre', '').strip()
    email = data.get('email', '').strip()
    telefono = data.get('telefono', '').strip()
    interes = data.get('interes', '').strip()

    if not all([nombre, email, telefono, interes]):
        return jsonify({'error': 'Faltan campos requeridos'}), 400
    if not EMAIL_REGEX.match(email):
        return jsonify({'error': 'Email inválido'}), 400
    if not PHONE_REGEX.match(telefono):
        return jsonify({'error': 'Teléfono inválido'}), 400

    nuevo = Contacto(nombre=nombre, email=email, telefono=telefono, interes=interes)
    db.session.add(nuevo)
    db.session.commit()

    return jsonify({'mensaje': 'Contacto guardado con éxito'}), 201

# /api/registros
@app.route('/api/registros', methods=['GET'])
def registros():
    contactos = Contacto.query.order_by(Contacto.fecha.desc()).all()
    resultado = [{
        'id': c.id,
        'nombre': c.nombre,
        'email': c.email,
        'telefono': c.telefono,
        'interes': c.interes,
        'fecha': c.fecha.isoformat()
    } for c in contactos]
    return jsonify(resultado), 200
