from datetime import datetime

import peewee

from app.v1.utils.db import db


class Book(peewee.Model):
    title = peewee.CharField()
    author = peewee.CharField()
    category = peewee.CharField()
    language = peewee.CharField()
    state = peewee.CharField()
    days_limit = peewee.IntegerField()
    location = peewee.CharField()
    pages_number = peewee.IntegerField()
    edition = peewee.IntegerField()
    created_at = peewee.DateTimeField(default=datetime.now)
    updated_at = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = db