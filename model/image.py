from model.base import BaseModel
from peewee import IntegerField, CharField

class Image(BaseModel):
    url = CharField()

    class Meta:
        db_table = 'image'