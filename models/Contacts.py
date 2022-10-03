from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from models.Users import UserBase

class ContactBase(BaseModel):
    id : Optional[int] = None
    nombre : str
    alias : Optional[str]
    correo : EmailStr
    telefono : Optional[str] = None
    celular : Optional[str]
    direccion : Optional[str]
    ciudad : Optional[str]
    estado : Optional[str]
    created_at : Optional[datetime]
    updated_at : Optional[datetime]
    class Config:
        orm_mode = True
