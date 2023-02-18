from fastapi import APIRouter, UploadFile, File, Depends
from ..utils.SymbolToBuyReq import SymbolToBuyReq
from ..managers.MainProcessManager import MainProcessManager

router = APIRouter(tags=["buy_and_sell_controller"])

@router.post(
    "/buy_and_sell/",
    status_code=200
)
def get_tax_calc(req: SymbolToBuyReq):
    x = 8
    return MainProcessManager().start_buy_and_sell_process(req)
