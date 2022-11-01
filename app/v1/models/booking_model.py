import peewee
from datetime import datetime

from app.v1.utils.db import db
from .user_model import User
from .book_model import Book

class Booking(peewee.Model):
    date_booking=  peewee.DateTimeField()
    user_id = peewee.ForeignKeyField(User,backref='booking')
    book_id =peewee.ForeignKeyField(Book,backref='booking')
    created_at=  peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = db