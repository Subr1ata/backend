from schema.base import BaseSchema

class Category(BaseSchema):
    id: int
    name: str
    parent: int = None
    logo: str = None

class CategoryCreate(BaseSchema):
    name: str
    parent: int = None
    logo: str = None