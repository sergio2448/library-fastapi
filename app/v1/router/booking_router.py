from fastapi import APIRouter, Depends, Body, status, Path

from typing import List

from app.v1.schema import booking_schema
from app.v1.service import booking_service
from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1")

@router.post(
    "/booking",
    tags=["bookings"],
    status_code=status.HTTP_201_CREATED,
    response_model=booking_schema.Booking,
    dependencies=[Depends(get_db)]
)
def add_booking(booking: booking_schema.BookingBase = Body(...)):
    return booking_service.add_booking(booking)

@router.get(
    "/bookings/{user_id}",
    tags=["bookings"],
    status_code=status.HTTP_200_OK,
    response_model=List[booking_schema.Booking],
    dependencies=[Depends(get_db)]
)
def get_bookings_by_user_id(
    user_id: int = Path(
        ...,
        gt=0
    )
):
    return booking_service.get_booking_by_user_id(user_id)


@router.get(
    "/booking/{booking_id}",
    tags=["bookings"],
    status_code=status.HTTP_200_OK,
    response_model=booking_schema.Booking,
    dependencies=[Depends(get_db)]
)
def get_booking(
    booking_id: int = Path(
        ...,
        gt=0
    )
):
    return booking_service.get_booking(booking_id)

@router.delete(
    "/{booking_id}/",
    tags=["bookings"],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(get_db)]
)
def delete_booking(
    booking_id: int = Path(
        ...,
        gt=0
    ),
    #current_user: User = Depends(get_current_user)
):
    booking_service.delete_booking(booking_id)

    return {
        'msg': 'Booking has been deleted successfully'
    }