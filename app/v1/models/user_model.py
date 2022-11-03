import peewee
from datetime import datetime

from app.v1.utils.db import db

class User(peewee.Model):

    email = peewee.CharField(unique=True)
    first_name = peewee.CharField()
    last_name =peewee.CharField()
    address = peewee.CharField()
    phone_number =peewee.CharField()
    state = peewee.CharField()
    gender = peewee.CharField()
    created_at=  peewee.DateTimeField(default=datetime.now)
    updated_at = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = db