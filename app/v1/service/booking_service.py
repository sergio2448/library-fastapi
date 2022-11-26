from fastapi import HTTPException, status

from app.v1.schema import booking_schema
from app.v1.models.booking_model import Booking as BookingModel


def add_booking(booking: booking_schema.Booking):

    db_booking = BookingModel(
        date_booking = booking.date_booking,
        user_id = booking.user_id,
        book_id = booking.book_id,
        created_at = booking.created_at,
    )

    db_booking.save()

    return booking_schema.Booking(
        id = db_booking.id,
        date_booking = booking.date_booking,
        user_id = booking.user_id,
        book_id = booking.book_id,
        created_at = booking.created_at,
    )

def get_bookings():

    """ if(is_done is None):
        tasks_by_user = BookingModel.filter(BookingModel.user_id == user.id).order_by(BookingModel.created_at.desc())
    else:
        tasks_by_user = BookingModel.filter((BookingModel.user_id == user.id) & (BookingModel.is_done == is_done)).order_by(BookingModel.created_at.desc()) """
    bookings = BookingModel.filter(BookingModel.id == BookingModel.id).order_by(BookingModel.created_at.desc())

    list_bookings = []
    for booking in bookings:
        list_bookings.append(
            booking_schema.Booking(
                id = booking.id,
                date_booking = booking.date_booking,
                user_id = booking.user_id.id,
                book_id = booking.book_id.id,
                created_at = booking.created_at,
            )
        )

    return list_bookings

def get_booking(booking_id: int):
    booking = BookingModel.filter((BookingModel.id == booking_id)).first()

    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )

    return booking_schema.Booking(
        id = booking.id,
        date_booking = booking.date_booking,
        user_id = booking.user_id.id,
        book_id = booking.book_id.id,
        created_at = booking.created_at,
    )

def delete_booking(booking_id: int):
    booking = BookingModel.filter((BookingModel.id == booking_id)).first()

    if not booking:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Booking not found"
        )

    booking.delete_instance()