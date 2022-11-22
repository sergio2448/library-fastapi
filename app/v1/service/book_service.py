from fastapi import HTTPException, status

from app.v1.schema import book_schema
from app.v1.models.book_model import Book as BookModel


def add_book(book: book_schema.Book):

    db_book = BookModel(
        title = book.title,
        author = book.author,
        category = book.category,
        language = book.language,
        state = book.state,
        days_limit = book.days_limit,
        location = book.location,
        pages_number = book.pages_number,
        edition = book.edition,
        created_at = book.created_at,
        updated_at = book.updated_at
    )

    db_book.save()

    return book_schema.Book(
        id = db_book.id,
        title = book.title,
        author = book.author,
        category = book.category,
        language = book.language,
        state = book.state,
        days_limit = book.days_limit,
        location = book.location,
        pages_number = book.pages_number,
        edition = book.edition,
        created_at = book.created_at,
        updated_at = book.updated_at
    )

def get_books():

    """ if(is_done is None):
        tasks_by_user = BookModel.filter(BookModel.user_id == user.id).order_by(BookModel.created_at.desc())
    else:
        tasks_by_user = BookModel.filter((BookModel.user_id == user.id) & (BookModel.is_done == is_done)).order_by(BookModel.created_at.desc()) """
    books = BookModel.filter(BookModel.id == BookModel.id).order_by(BookModel.created_at.desc())

    list_books = []
    for book in books:
        list_books.append(
            book_schema.Book(
                id = book.id,
                title = book.title,
                author = book.author,
                category = book.category,
                language = book.language,
                state = book.state,
                days_limit = book.days_limit,
                location = book.location,
                pages_number = book.pages_number,
                edition = book.edition,
                created_at = book.created_at,
                updated_at = book.updated_at
            )
        )

    return list_books

def get_book(book_id: int):
    book = BookModel.filter((BookModel.id == book_id)).first()

    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found"
        )

    return book_schema.Book(
        id = book.id,
        title = book.title,
        author = book.author,
        category = book.category,
        language = book.language,
        state = book.state,
        days_limit = book.days_limit,
        location = book.location,
        pages_number = book.pages_number,
        edition = book.edition,
        created_at = book.created_at,
        updated_at = book.updated_at
    )

@router.patch(
    "/{book_id}/state",
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
    "/{book_id}/",
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