from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

@router.get('/')
def get_images(path):
    return FileResponse(path)