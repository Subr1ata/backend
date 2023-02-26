from schema.base import BaseSchema

class Category(BaseSchema):
    id: int
    name: str
    parent: int = None
    logo: str = None

