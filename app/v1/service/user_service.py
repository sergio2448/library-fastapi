# Aquí irán las funciones relacionadas con el CRUD de los Usuarios

# Importaciones
from fastapi import HTTPException, status
from app.v1.models.user_model import User as UserModel
from app.v1.schema import user_schema

# crear usuario
def create_user(user: user_schema.UserBase):
    
    get_user = UserModel.filter((UserModel.email == user.email) | (UserModel.username == user.username)).first()
    if get_user:
        msg = "Email already registered"
        if get_user.username == user.username:
            msg = "Username already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )
    db_user = UserModel(
        user_email = user.email,
        user_first_name = user.first_name,
        user_last_name = user.last_name,
        user_address = user.address,
        user_phone_number = user.phone_number,
        user_state = user.state,
        user_gender = user.gender,
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