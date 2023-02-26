from model.base import BaseModel
from peewee import IntegerField, CharField, ForeignKeyField
from model.category import Category
from model.image import Image

class Product(BaseModel):
    category = ForeignKeyField(Category, column_name='category')
    cost = IntegerField()
    price = IntegerField()
    star = IntegerField()
    img = ForeignKeyField(Image, column_name='image')
    description = CharField()
    sales = IntegerField()
    comment = CharField()
    ship_comment = CharField()

    class Meta:
        db_table = 'product'