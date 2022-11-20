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