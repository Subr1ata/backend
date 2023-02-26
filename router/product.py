from typing import List
from fastapi import APIRouter, UploadFile
from model.image import Image
from model.product import Product
from schema import product as schema

router = APIRouter()


@router.get('/', response_model=List[schema.Product])
def get_product():
    return Product.get_list()


@router.post('/')
def create_product(product: schema.ProductBase):
    img = Image.create(product.image)

    product = product.dict()
    product['image'] = [img.id]
    return Product.create(**product)
