from pydantic import BaseModel, EmailStr

class ContactoCreateSchema(BaseModel):
    nombre: str
    email: EmailStr
    telefono: str
    interes: str

from datetime import datetime

class ContactoSchema(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    telefono: str
    interes: str
    fecha: datetime