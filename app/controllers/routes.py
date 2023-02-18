from fastapi import APIRouter
from app.controllers import buy_and_sell_controller

api_router = APIRouter()

api_router.include_router(buy_and_sell_controller.router)