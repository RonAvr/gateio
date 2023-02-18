from pydantic import BaseModel


class SymbolToBuyReq(BaseModel):
    symbol: str = None
