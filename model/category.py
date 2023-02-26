from model.base import BaseModel
from peewee import IntegerField, CharField

class Category(BaseModel):
    parent = IntegerField()
    logo = CharField()

    class Meta:
        db_table = 'category'