from model.base import BaseModel
from peewee import IntegerField, CharField, ForeignKeyField
from model.category import Category
from model.image import Image
from playhouse.postgres_ext import ArrayField

class Product(BaseModel):
    category = ForeignKeyField(Category, column_name='category')
    cost = IntegerField()
    price = IntegerField()
    star = IntegerField()
    image = ArrayField()
    description = CharField()
    sales = IntegerField()
    comment = CharField()
    ship_comment = CharField()

    class Meta:
        db_table = 'product'

    @classmethod
    def get_list(cls):
        return list(cls.select())