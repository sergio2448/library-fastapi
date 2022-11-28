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
    return lending_service.add_lending(lending)

@router.get(
    "/lendings",
    tags=["lendings"],
    status_code=status.HTTP_200_OK,
    response_model=List[lending_schema.Lending],
    dependencies=[Depends(get_db)]
)
def get_lendings():
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
    "/lending/{user_id}",
    tags=["lendings"],
    status_code=status.HTTP_200_OK,
    response_model=lending_schema.Lending,
    dependencies=[Depends(get_db)]
)
def get_lending_user_id(
    user_id: int = Path(
        ...,
        gt=0
    )
):
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
    lending_service.delete_lending(lending_id)

    return {
        'msg': 'Lending has been deleted successfully'
    }