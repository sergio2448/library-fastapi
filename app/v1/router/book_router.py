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
    """
    ## Create a new book in the app

    ### Args
    The app can recive next fields into a JSON
    - title: title of the book.
    - author: book's author.
    - category: book genre
    - language: language in which it is written.
    - state: state of de book: available, non available, booking.
    - days_limit: days limit for lending.
    - location: location in the library.
    - pages_number: number of pages.
    - edition: edition of the book
    - created_at: datetime
    - updated_at: datime

    ### Returns
    - book: Book info
    """
    return book_service.add_book(book)

@router.get(
    "/books",
    tags=["books"],
    status_code=status.HTTP_200_OK,
    response_model=List[book_schema.Book],
    dependencies=[Depends(get_db)]
)
def get_books():
    """
    ## get all the books.

    ### Args
    Do not receive args

    ### Returns
    - Array:  array whose elementes are the Books info(dicts)
    """
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
    """
    ## Get one Book.

    ### Args
    The app can recive next fields into a JSON
    - book_id: id of the desired book.

    ### Returns
    - book: Book info
    """
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
    
):
    """
    ## update the state of a book.

    ### Args
    The app can recive next fields into a JSON
    - book_id: id of the desired book.
    - state: state of de book: available, non available, booking.

    ### Returns
    - book: Book info
    """
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
    
):
    """
    ## Delete a book.

    ### Args
    The app can recive next fields into a JSON
    - book_id: id of the desired book.

    ### Returns
    - string: that confirms the successfull delete of the book.
    """
    book_service.delete_book(book_id)

    return {
        'msg': 'Book has been deleted successfully'
    }