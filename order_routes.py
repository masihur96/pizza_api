
from fastapi import APIRouter

order_router = APIRouter(
    prefix="/orders",
    tags=['order']
)


@order_router.get('/')
async def hello():
    return {"message": "Hello Orders"}
