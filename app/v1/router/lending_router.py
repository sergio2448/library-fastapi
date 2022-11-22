from fastapi import APIRouter, Depends, Body, Path
from fastapi import status
from app.v1.schema import lending_schema
from app.v1.service import lending_service
from app.v1.utils.db import get_db
from app.v1.schema.user_schema import User
from app.v1.schema.book_schema import Book

router = APIRouter(prefix="/api/v1")

#create

@router.post(
    "/lending",
    tags=["lendings"],
    status_code=status.HTTP_201_CREATED,
    response_model= lending_schema.Lending,
    dependencies=[Depends(get_db)]
)
def create_lending(
    lending: lending_schema.LendingBase = Body(...),
    user: User = Body(...),
    book: Book = Body(...)
):
    return lending_service.create_lending(lending, user.id, book.id)

@router.get(
    "/{user_id}/last_lending",
    tags=["lendings"],
    status_code=status.HTTP_201_CREATED,
    response_model= lending_schema.Lending,
    dependencies=[Depends(get_db)]

)

def get_last_lending(
    user_id: int = Path(
        ...,
        gt=0
    )
):
    return lending_service.get_last_lending(user_id)


@router.get(
    "/user/{user_id}/lendings",
    tags=["lendings"],
    status_code=status.HTTP_201_CREATED,
    response_model= lending_schema.Lending,
    dependencies=[Depends(get_db)]

)

def get_lendings(
    user_id: int = Path(
        ...,
        gt=0
    )
):
    return lending_service.get_lending(user_id)








@router.delete(
   " lending/{lending_id}/",
    tags=["lendings"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_delete(
    lending_id: int = Path(
        ...,
        gt=0
    ),
    #current_user: User = Depends(get_current_user)
):
    lending_service.delete_lending(lending_id)

    return {
        'msg': 'lending has been deleted successfully'
    }