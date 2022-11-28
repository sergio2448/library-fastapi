from fastapi import APIRouter, Depends, Body, status, Path

from typing import List

from app.v1.schema import book_schema
from app.v1.service import book_service
from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/book",
    tags=["books"],
    status_code=status.HTTP_201_CREATED,
    response_model=book_schema.Book,
    dependencies=[Depends(get_db)]
)
def add_book(book: book_schema.BookBase = Body(...)):
    return book_service.add_book(book)

@router.get(
    "/books",
    tags=["books"],
    status_code=status.HTTP_200_OK,
    response_model=List[book_schema.Book],
    dependencies=[Depends(get_db)]
)
def get_books():
    return book_service.get_books()


@router.get(
    "/book/{book_id}",
    tags=["books"],
    status_code=status.HTTP_200_OK,
    response_model=book_schema.Book,
    dependencies=[Depends(get_db)]
)
def get_book(
    book_id: int = Path(
        ...,
        gt=0
    )
):
    return book_service.get_book(book_id)

@router.patch(
    "/book/{book_id}/state",
    tags=["books"],
    status_code=status.HTTP_200_OK,
    response_model=book_schema.Book,
    dependencies=[Depends(get_db)]
)
def update_book(
    book_state: str = Body(...),
    book_id: int = Path(
        ...,
        gt=0
    ),
    #current_user: User = Depends(get_current_user)
):
    return book_service.update_state_book(book_state, book_id)

@router.delete(
    "/book/{book_id}",
    tags=["books"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_book(
    book_id: int = Path(
        ...,
        gt=0
    ),
    #current_user: User = Depends(get_current_user)
):
    book_service.delete_book(book_id)

    return {
        'msg': 'Book has been deleted successfully'
    }