'''
En este archivo crearemos el modelo User de Pydantic, esto nos ayudará a validar los tipos de datos
a la hora de crear un Usuario.
'''
# importaciones necesarias
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from enum import Enum

# Definimos el primer modelo de Pydantic

class UserState(Enum):
    pending_payments = "pending_payments"
    ok = "ok"

class UserBase(BaseModel):
    email: EmailStr = Field(
        ...,
    )
    first_name: str = Field(
        ...,
        min_length=3,
        max_length=30
    )
    last_name: str = Field(
        ...,
        min_length=3,
        max_length=30
    )
    address: str = Field(
        ...,
        min_length=5,
        max_length=30
    )
    phone_number: str = Field(
        ...,
        min_length=3,
        max_length=30
    )
    state: UserState = Field(...)
    gender: str = Field(...)
    created_at: datetime = Field(default=datetime.now())
    updated_at: datetime = Field(default=datetime.now())

class User(UserBase):
    id: int = Field(...)
