# Creamos la rutas asociadas al usuario

# importaciones
from fastapi import APIRouter, Depends, status, Body, Path
from app.v1.schema import user_schema
from app.v1.service import user_service
from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")
#Create User
@router.post(
    "/user",
    tags=["users"],
    status_code= status.HTTP_201_CREATED,
    response_model= user_schema.User,
    dependencies= [Depends(get_db)],
    summary= "Create a new user"
)
def create_user(user: user_schema.UserBase = Body(...)):

    """
    ## Create a new user in the app

    ### Args
    The app can recive next fields into a JSON
    - email: A valid email
    - first_name: string minimun of 3 char
    - last_name: string minimun of 3 char
    - address: string minimun of 5 char
    - phone_number: string minimun of 3 char
    - state: string, "available" is deafult.
    - gender: string "M" or "F"
    - created_at: datetime
    - updated_at: datime

        Returns
        - user: User info
    """
    return user_service.create_user(user)

# Update User
@router.patch(
    "/user/{user_id}/edit",
    tags=["users"],
    status_code=status.HTTP_200_OK,
    response_model=user_schema.UserBase,
    dependencies=[Depends(get_db)]
)
def edit_user(
    user_id: int = Path(
        ...,
        gt=0
    ), 
        user: user_schema.UserBase = Body(...) 
    ):
  
    """
    ## Update an User in the app

    ### Args
    The app can recive next fields into a JSON
    - email: A valid email
    - first_name: string minimun of 3 char
    - last_name: string minimun of 3 char
    - address: string minimun of 5 char
    - phone_number: string minimun of 3 char
    - state: string, "available" is deafult.
    - gender: string "M" or "F"
    - created_at: datetime
    - updated_at: datime

    ### Returns
    - user: User info
    
    """
    return user_service.update_user(user_id, user)  

# Delete User
@router.delete(
    "/user/{user_id}/",
    tags=["users"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_user(
    user_id: int = Path(
        ...,
        gt=0
    ),
    ):
    """
    ## Delete an user from the app

    ### Args
    The function receive
    - user_id: from an registered user.

    ### Returns
    - string: that confirms a succesfull delete.
    """
    user_service.delete_user(user_id)


    return {
        'msg': f'User with id: {user_id}, has been deleted successfully'
    }