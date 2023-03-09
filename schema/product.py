from schema.base import BaseSchema
from fastapi import UploadFile
from typing import List

class ProductBase(BaseSchema):
    name: str
    category: int
    cost: int
    price: int
    star: int = 5
    image: str
    description: str = None
    sales: int = 0
    comment: str = None
    ship_comment: str = None

class Product(BaseSchema):
    id: int

class ProductCreate(BaseSchema):
    pass