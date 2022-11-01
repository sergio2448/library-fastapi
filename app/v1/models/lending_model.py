import peewee
from datetime import datetime

from app.v1.utils.db import db
from .user_model import User
from .book_model import Book

class Lending(peewee.Model):
    start_at=  peewee.DateTimeField()
    end_at = peewee.DateTimeField()
    user_id = peewee.ForeignKeyField(User,backref='lending')
    book_id =peewee.ForeignKeyField(Book,backref='lending')
    created_at=  peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = db