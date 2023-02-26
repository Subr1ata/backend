from fastapi import APIRouter
from model.product import Product
from schema import product as schema
from typing import List

router = APIRouter()

@router.get('/', response_model=List[schema.Product])
def get_product():
    return Product.get_list()


@router.post('/', response_model=schema.Product)
def create_product(product: schema.ProductCreate):
    return Product.create(**product.dict())