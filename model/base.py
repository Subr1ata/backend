from peewee import CharField, Model, BooleanField

from config.database import db


class BaseModel(Model):
    name = CharField()
    active = BooleanField()

    class Meta:
        database = db