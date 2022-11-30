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
    return penalty_service.add_penalty(penalty)

@router.get(
    "/penalties",
    tags=["penalties"],
    status_code=status.HTTP_200_OK,
    response_model=List[penalty_schema.Penalty],
    dependencies=[Depends(get_db)]
)
def get_penalties():
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
    return penalty_service.get_penalty(penalty_id)

@router.get(
    "/penalty/{user_id}/user",
    tags=["penalties"],
    status_code=status.HTTP_200_OK,
    response_model=List[penalty_schema.Penalty],
    dependencies=[Depends(get_db)]
)
def get_penalty_user_id(
    user_id: int = Path(
        ...,
        gt=0
    )
):
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
    #current_user: User = Depends(get_current_user)
):
    penalty_service.delete_penalty(penalty_id)

    return {
        'msg': 'Penalty has been deleted successfully'
    }