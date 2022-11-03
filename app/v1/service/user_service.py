# Aquí irán las funciones relacionadas con el CRUD de los Usuarios

# Importaciones
from fastapi import HTTPException, status
from app.v1.models.user_model import User as UserModel
from app.v1.schema import user_schema

# crear usuario
def create_user(user: user_schema.User):
    db_user = UserModel(
        email = user.email,
        first_name = user.first_name,
        last_name = user.last_name,
        address = user.address,
        phone_number = user.phone_number,
        state = user.state,
        gender = user.gender,
        created_at = user.created_at,
        update_at = user.updated_at
    )
    db_user.save()

    return user_schema.User(
        id = db_user.id,
        first_name= db_user.first_name,
        last_name= db_user.last_name,
        address=db_user.address,
        email = db_user.email,
        phone_number=db_user.phone_number,
        state=db_user.state,
        gender=db_user.gender,
        created_at=db_user.created_at,
        updated_at=db_user.updated_at
    )

# update user
def update_user(user_id: int, user: user_schema.User):
        db_user = UserModel.filter(UserModel.id == user_id).first()

        db_user.first_name = user.first_name
        db_user.last_name = user.last_name
        db_user.address = user.address
        db_user.email = user.email
        db_user.phone_number = user.phone_number
        db_user.state = user.state
        db_user.gender = user.gender

        db_user.save()

        return user_schema.User(
        id = db_user.id,
        first_name= db_user.first_name,
        last_name= db_user.last_name,
        address=db_user.address,
        email = db_user.email,
        phone_number=db_user.phone_number,
        state=db_user.state,
        gender=db_user.gender,
        created_at=db_user.created_at,
        updated_at=db_user.updated_at
    )
        
