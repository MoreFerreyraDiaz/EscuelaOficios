from . import db
from datetime import DateTime

class Contacto(db.Model):
    __tablename__ = 'Contactos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    interes = db.Column(db.String(50), nullable=False)
    fecha = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self) -> str:
        return f"<Contacto {self.nombre}>"
    