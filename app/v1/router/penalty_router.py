from fastapi import APIRouter, Depends, Body, status, Path

from typing import List

from app.v1.schema import penalty_schema
from app.v1.service import penalty_service
from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/penalty",
    tags=["penalties"],
    status_code=status.HTTP_201_CREATED,
    response_model=penalty_schema.Penalty,
    dependencies=[Depends(get_db)]
)
def add_penalty(penalty: penalty_schema.PenaltyBase = Body(...)):
    """
    ## Create a new penalty in the app

    ### Args
    The app can recive next fields into a JSON
    - days_late: number of days after the end date of a lending.
    - total_taxes: total amount of the penalty.
    - state: state of the penalty: cancelled or non cancelled.
    - lending_id: id of the lending associated.
    - created_at: datetime

    ### Returns
    - penalty: penalty info
    """
    return penalty_service.add_penalty(penalty)

@router.get(
    "/penalties",
    tags=["penalties"],
    status_code=status.HTTP_200_OK,
    response_model=List[penalty_schema.Penalty],
    dependencies=[Depends(get_db)]
)
def get_penalties():
    """
    ## Get all penalties

    ### Args
    Do not receive args.

    ### Returns
    - array: whose elements are penalties(dicts).
    """  
    return penalty_service.get_penalties()


@router.get(
    "/penalty/{penalty_id}",
    tags=["penalties"],
    status_code=status.HTTP_200_OK,
    response_model=penalty_schema.Penalty,
    dependencies=[Depends(get_db)]
)
def get_penalty(
    penalty_id: int = Path(
        ...,
        gt=0
    )
):
    """
    ## Get a penalty by Id

    ### Args
    - penalty_id: id of the desired penalty.

    ### Returns
    - penalty: penalty info
    """
    return penalty_service.get_penalty(penalty_id)

@router.get(
    "/penalty/{user_id}",
    tags=["penalties"],
    status_code=status.HTTP_200_OK,
    response_model=penalty_schema.Penalty,
    dependencies=[Depends(get_db)]
)
def get_penalty_user_id(
    user_id: int = Path(
        ...,
        gt=0
    )
):  
    """
    ## Get all penalties from an user

    ### Args
    - user_id: id of the desired user.

    ### Returns
    - array: whose elements are the penalties of the given user.
    """
    return penalty_service.get_penalties_by_user_id(user_id)

@router.delete(
    "/penalty/{penalty_id}",
    tags=["penalties"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_penalty(
    penalty_id: int = Path(
        ...,
        gt=0
    ),
):  
    
    """
    ## Delete a penalty

    ### Args
    - penalty_id: id of the desired penalty.

    ### Returns
    - string: that confirms the successfull delete.
    """
    penalty_service.delete_penalty(penalty_id)

    return {
        'msg': 'Penalty has been deleted successfully'
    }