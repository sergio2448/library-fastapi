from datetime import datetime

import peewee

from app.v1.utils.db import db



class Book(peewee.Model):
    title = peewee.CharField()
    author = peewee.CharField()
    category = peewee.CharField()
    language = peewee.CharField()
    state = peewee.CharField()
    created_at = peewee.DateTimeField(default=datetime.now)
    days_limit = peewee.IntegerField()
    location = peewee.CharField()
    pages_number = peewee.IntegerField()
    edition = peewee.IntegerField()

    class Meta:
        database = db