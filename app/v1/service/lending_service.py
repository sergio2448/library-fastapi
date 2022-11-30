from fastapi import HTTPException, status

from app.v1.schema import lending_schema
from app.v1.models.lending_model import Lending as LendingModel
from app.v1.service.book_service import get_book
from app.v1.service.user_service import get_user_by_id


def add_lending(lending: lending_schema.Lending):

    book = get_book(lending.book_id)
    user = get_user_by_id(lending.user_id)

    db_lending = LendingModel(
        start_at = lending.start_at,
        end_at = lending.end_at,
        user_id = lending.user_id,
        book_id = lending.book_id,
        created_at = lending.created_at,
    )

    if (str(book.state) == "BookState.Available" and str(user.state) == "UserState.ok"):
        db_lending.save()
    elif str(book.state) != "BookState.Available":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book {book.state}"
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User has {user.state}"
        )

    return lending_schema.Lending(
        id = db_lending.id,
        start_at = lending.start_at,
        end_at = lending.end_at,
        user_id = lending.user_id,
        book_id = lending.book_id,
        created_at = lending.created_at
    )

def get_lendings():

    """ if(is_done is None):
        tasks_by_user = LendingModel.filter(LendingModel.user_id == user.id).order_by(LendingModel.created_at.desc())
    else:
        tasks_by_user = LendingModel.filter((LendingModel.user_id == user.id) & (LendingModel.is_done == is_done)).order_by(LendingModel.created_at.desc()) """
    lendings = LendingModel.filter(LendingModel.id == LendingModel.id).order_by(LendingModel.created_at.desc())

    list_lendings = []
    for lending in lendings:
        list_lendings.append(lending_schema.Lending(
                id = lending.id,
                start_at = lending.start_at,
                end_at = lending.end_at,
                user_id = lending.user_id.id,
                book_id = lending.book_id.id,
                created_at = lending.created_at,
            )
        )

    return list_lendings

def get_lending(lending_id: int):
    lending = LendingModel.filter((LendingModel.id == lending_id)).first()

    if not lending:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lending not found"
        )

    return lending_schema.Lending(
        id = lending.id,
        start_at = lending.start_at,
        end_at = lending.end_at,
        user_id = lending.user_id.id,
        book_id = lending.book_id.id,
        created_at = lending.created_at
    )

def get_lendings_by_user_id(user_id: int):


    lendings = LendingModel.filter(LendingModel.user_id == user_id).order_by(LendingModel.start_at.desc())

    if not lendings:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id: {user_id} has not lendings"
        )

    list_lendings = []
    for lending in lendings:

        list_lendings.append(
            lending_schema.Lending(

                id = lending.id,
                start_at = lending.start_at,
                end_at = lending.end_at,
                user_id = lending.user_id.id,
                book_id = lending.book_id.id,
                created_at = lending.created_at,
            )
        )

    return list_lendings


def delete_lending(lending_id: int):

    lending = LendingModel.filter((LendingModel.id == lending_id)).first()
    if not lending:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lending not found"
        )


    lending.delete_instance()

