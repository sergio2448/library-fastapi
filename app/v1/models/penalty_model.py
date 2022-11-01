import peewee
from datetime import datetime

from app.v1.utils.db import db
from .lending_model import Lending

class Penalty(peewee.Model):
    days_late= peewee.IntegerField()
    total_taxes= peewee.IntegerField()
    state= peewee.CharField()
    lending_id= peewee.ForeignKeyField(Lending,backref='penalty')
    created_at=  peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = db