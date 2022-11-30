from fastapi import APIRouter, Depends, Body, status, Path

from typing import List

from app.v1.schema import lending_schema
from app.v1.service import lending_service
from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/lending",
    tags=["lendings"],
    status_code=status.HTTP_201_CREATED,
    response_model=lending_schema.Lending,
    dependencies=[Depends(get_db)]
)
def add_lending(lending: lending_schema.LendingBase = Body(...)):
    """
    ## Create a new lending in the app

    ### Args
    The app can recive next fields into a JSON
    - start_at: Begin date of the lending.
    - end_at: End date of the lending.
    - user_id: id of the user.
    - book_id: id of the book that will be borrowed.
    - created_at: datetime
    - updated_at: datime

    ### Returns
    - lending: lending info
    """
    return lending_service.add_lending(lending)

@router.get(
    "/lendings",
    tags=["lendings"],
    status_code=status.HTTP_200_OK,
    response_model=List[lending_schema.Lending],
    dependencies=[Depends(get_db)]
)
def get_lendings():

    """
    ## Get all lendings.

    ### Args
    Do not receive args.
    ### Returns
    - array: whose elements are the lendings(dicts with lending info)
    """

    return lending_service.get_lendings()


@router.get(
    "/lending/{lending_id}",
    tags=["lendings"],
    status_code=status.HTTP_200_OK,
    response_model=lending_schema.Lending,
    dependencies=[Depends(get_db)]
)
def get_lending(
    lending_id: int = Path(
        ...,
        gt=0
    )
):

    return lending_service.get_lending(lending_id)

@router.get(
    "/lending/{user_id}/user",
    tags=["lendings"],
    status_code=status.HTTP_200_OK,
    response_model=List[lending_schema.Lending],

    """
    ## Get a lending.

    ### Args
    - lending_id: id of the desired lending.
    ### Returns
    - lending: Lending info
    """
    return lending_service.get_lending(lending_id)


    dependencies=[Depends(get_db)]
)
def get_lending_user_id(
    user_id: int = Path(
        ...,
        gt=0
    )

):

    """
    ## Get all lendings from a user.

    ### Args
    - user_id: user id.
    ### Returns
    - array: whose elements are the lendings mada by the user with that id
    """

    return lending_service.get_lendings_by_user_id(user_id)

@router.delete(
    "/lending/{lending_id}",
    tags=["lendings"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_lending(
    lending_id: int = Path(
        ...,
        gt=0
    ),

    #current_user: User = Depends(get_current_user)
):
  
    """
    ## Delete a lending.

    ### Args
    - lending_id: id of the desired lending.
    ### Returns
    - string: that confirms the successfull delete.
    """

    lending_service.delete_lending(lending_id)

    return {
        'msg': 'Lending has been deleted successfully'
    }