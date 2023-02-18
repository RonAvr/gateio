from app.managers.EmailManager import EmailManager
from app.managers.GateClient import GateClient
from app.utils.SymbolToBuyReq import SymbolToBuyReq
import time


class MainProcessManager:

    def __init__(self):
        self.email_manager = EmailManager()
        self.gate_client = GateClient()
        self.delay = 60

    def __get_current_symbol_price(self, symbol: str):
        price = self.gate_client.get_rate(symbol=symbol)
        return 1.005 * price

    def __get_amount_to_buy(self, price):
        balance = self.gate_client.get_currency_balance()
        return balance/price

    def start_buy_and_sell_process(self, req: SymbolToBuyReq):
        symbol = req.symbol
        if self.gate_client.is_pair_exists(symbol):

            price = self.__get_current_symbol_price(symbol)
            amount = self.__get_amount_to_buy(price)
            self.gate_client.buy_order(symbol=symbol, rate=price, amount=amount)

            t_0 = time.time()
            self.email_manager.send_email(symbol=symbol, price=price, amount=amount)

            # waiting to execute the sell order
            t = time.time()
            dt = t - t_0
            while (dt < self.delay):
                t = time.time()
                dt = t - t_0

            self.gate_client.sell_order(symbol=symbol)
            new_price = self.__get_current_symbol_price(symbol)
            self.email_manager.send_email(symbol=symbol, amount=amount, price=new_price, method="sell")

if __name__ == '__main__':
    x = MainProcessManager()
    req = SymbolToBuyReq()
    req.symbol = "BTC"
    x.start_buy_and_sell_process(req)
    pass

