from schema.base import BaseSchema

class ProductBase(BaseSchema):
    name: str
    category: int
    cost: int
    price: int
    star: int = 5
    image: int
    description: str = None
    sales: int = 0
    comment: str = None
    ship_comment: str = None

class Product(BaseSchema):
    id: int

class ProductCreate(BaseSchema):
    pass