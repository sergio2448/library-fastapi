from fastapi import HTTPException, status
from app.v1.schema import lending_schema
from app.v1.models.lending_model import Lending as LendingModel
from app.v1.schema import user_schema
from app.v1.schema import book_schema

def create_lending(lending: lending_schema.Lending):

    db_lending = LendingModel(
        start_at = lending.start_at,
        end_at = lending.end_at,
        user_id = lending.user_id,
        book_id = lending.book_id,
        created_at = lending.created_at
    )

    db_lending.save()

    return lending_schema.Lending(
        id = db_lending.id,
        start_at= db_lending.start_at,
        end_at= db_lending.end_at,
        user_id = lending.user_id,
        book_id = lending.book_id,
        created_at = db_lending.created_at
    )

def get_last_lending(user_id: int):
    lending = LendingModel.filter(LendingModel.user_id == user_id).first()
    if not lending:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The User has not lendings"
        )
    return lending_schema.Lending(
        id = lending.id,
        start_at= lending.start_at,
        end_at= lending.end_at,
        created_at = lending.created_at
    )

def get_lending(user_id: int):
    lendings = LendingModel.filter(LendingModel.user_id == user_id).order_by(LendingModel.created_at.desc())

    lendings_list = []
    for lending in lendings:
        lendings_list.append(
            lending_schema.Lending(
                id = lending.id,
                start_at = lending.start_at,
                end_at=lending.end_at,
                user_id= lending.user_id,
                book_id= lending.book_id,
                created_at= lending.created_at
            )
        )
    return lendings_list

  



def delete_lending(lending_id: int):
    lending = LendingModel.filter((LendingModel.id == lending_id)).first()

    if not lending:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="lending not found"
        )

    lending.delete_instance()

