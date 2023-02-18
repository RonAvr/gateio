from pydantic import BaseModel


class TaxCalcReq(BaseModel):
    salaries: list[int] = []
    nz: list[int] = []
    arnona: int = None
    expanses: int = None
    cars: list[int] = []
    gasoline: int = None
