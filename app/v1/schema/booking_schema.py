from datetime import datetime

from pydantic import BaseModel
from pydantic import Field

class BookingBase(BaseModel):
    date_booking: datetime = Field(default=datetime.now())
    user_id: int = Field(...)
    book_id: int = Field(...)
    created_at = Field(default=datetime.now())

class Booking(BookingBase):
    id: int = Field(...)