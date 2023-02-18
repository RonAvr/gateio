from fastapi import APIRouter
from app.controllers import tax_calc_controller

api_router = APIRouter()

api_router.include_router(tax_calc_controller.router)