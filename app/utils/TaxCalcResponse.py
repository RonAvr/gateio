from pydantic import BaseModel


class TaxCalcResponse(BaseModel):
    direct_tax: int = None
    national_security: int = None
    health_insurance: int = None
    arnona: int = None
    vat: int = None
    car_tax: int = None
    gasoline_tax: int = None
