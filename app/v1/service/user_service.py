# Aquí irán las funciones relacionadas con el CRUD de los Usuarios

# Importaciones
from fastapi import HTTPException, status
from app.v1.models.user_model import User as UserModel
from app.v1.schema import user_schema

# crear usuario
def create_user(user: user_schema.User):

    get_user = UserModel.filter((UserModel.email == user.email) | (UserModel.phone_number == user.phone_number)).first()
    if get_user:
        msg = f"User with email {user.email} already registered"
        if get_user.phone_number == user.phone_number:
            msg = f"User with phone number {user.phone_number} already registered"
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=msg
        )

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

        if db_user.email != user.email:
            get_user = UserModel.filter((UserModel.email == user.email)).first()
            if get_user:
                msg = f"User with email {user.email} already registered"
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=msg
                )
        if db_user.phone_number != user.phone_number:
            get_user = UserModel.filter((UserModel.phone_number == user.phone_number)).first()
            if get_user:
                msg = f"User with phone number {user.phone_number} already registered"
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=msg
                )

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

#delete user

def delete_user(user_id: int):
    user = UserModel.filter((UserModel.id == user_id)).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    user.delete_instance()

