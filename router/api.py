from fastapi import APIRouter
from router import category, product, image

router = APIRouter()

router.include_router(
    category.router,
    prefix='/category',
    tags=['category']
)

router.include_router(
    product.router,
    prefix='/product',
    tags=['product']
)

router.include_router(
    image.router,
    prefix='/image',
    tags=['image']
)