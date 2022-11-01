from app.v1.models.user_model import User
from app.v1.models.book_model import Book
from app.v1.models.booking_model import Booking
from app.v1.models.lending_model import Lending
from app.v1.models.penalty_model import Penalty


from app.v1.utils.db import db

def create_tables():
    with db:
        db.create_tables([User, Book,Booking,Lending,Penalty])