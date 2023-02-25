from peewee import CharField, IntegerField, ForeignKeyField, BooleanField
import peewee

from sql_app.database import db


class Category(peewee.Model):
    name = CharField()
    parent = IntegerField()
    logo = CharField()
    active = BooleanField()

    class Meta:
        database = db
        db_table = 'category'