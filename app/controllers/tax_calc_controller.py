from fastapi import APIRouter, UploadFile, File, Depends
from ..utils.TaxCalcResponse import TaxCalcResponse
from ..utils.TaxCalcReq import TaxCalcReq
from ..managers.Extractor import TaxCalculator

router = APIRouter(tags=["tax_calc_controller"])

@router.post(
    "/get-tax-calc/",
    response_model=TaxCalcResponse,
    status_code=200
)
def get_tax_calc(req: TaxCalcReq):
    return TaxCalculator().get_tax_calculation(req)
