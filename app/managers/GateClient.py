from app.managers.gateAPI import GateIO
from app.managers.HttpUtil import getSign, httpGet, httpPost
from app.managers.logger import our_logger
import time
import ast
import logging

our_logger(name='main_gate_io', filename='main.log')
logger = (logging.getLogger('main_gate_io'))


class GateClient:

    # address
    btcAddress = 'your btc address'

    # Provide constants
    API_QUERY_URL = 'data.gateio.life'
    API_TRADE_URL = 'api.gateio.life'

    # 填写 apiKey APISECRET
    apiKey = 'BDB08F5B-CC49-4093-A514-BC9B2FC48F21'
    secretKey = 'b3ec29afcd9b99573238b37424775890beadeaa5bf7fddf89dcbeb0873191555'


    def __init__(self):
        self.API_QUERY_URL = self.API_QUERY_URL
        self.API_TRADE_URL = self.API_TRADE_URL
        self.apiKey = self.apiKey
        self.secretKey = self.secretKey
        self.gate_query = GateIO(self.API_QUERY_URL, self.apiKey, self.secretKey)
        self.gate_trade = GateIO(self.API_TRADE_URL, self.apiKey, self.secretKey)

    def is_pair_exists(self, symbol, pair="USDT"):
        """
        Function that checks if a specific trading pair exists in GateIO
        :param symbol: a crypto pair
        :param pair: a crypto pair
        :return: True if that paris exists in GateIO, False if not
        """
        pair = symbol.upper() +'_' +pair.upper()
        pairs = self.gate_query.pairs()
        if pair in pairs:
            logger.debug(f'Tha pair {pair} exists in GateIO')
            return True
        logger.debug(f"Tha pair {pair} doesn't exists in GateIO")
        return False

    def buy_order(self, symbol, rate, amount, pair="USDT"):
        """
        :param symbol: base currency
        :param rate: the rate of the crypto trade pair
        :param amount: the amount of currencies
        :param pair: the pair currency
        :return: a dictionary from GateIO API
        """
        order_pair = symbol.upper() +'_' + pair.upper()
        buy_result = self.gate_trade.buy(currencyPair=order_pair, amount=amount, rate=rate)
        logger.debug(f'Buy order: {amount} shares of {symbol}_{pair}')
        logger.debug(buy_result)
        return buy_result

    def sell_order(self, symbol, pair="USDT"):
        """
        :param symbol: base currency
        :param pair: the pair currency
        :param amount: the amount of currencies
        :return: selling crypto
        """
        order_pair = symbol.upper() +'_' + pair.upper()
        rate = self.get_rate(symbol)*0.995
        amount = self.get_currency_balance(symbol)
        sell_result = self.gate_trade.sell(currencyPair=order_pair, amount=amount, rate=rate)
        logger.debug(f'Sell order: {amount} shares of {symbol}_{pair}')
        logger.debug(sell_result)
        return sell_result

    def get_rate(self, symbol, pair="USDT"):
        """
        :param symbol: a base currency
        :param pair: pair currecny
        :return: the last price of the trading pair, if the trading pair doesn't exist return '-1'
        """
        rate_pair = symbol.upper() + "_" + pair.upper()
        URL = f"/api2/1/ticker/"
        result = httpGet(self.API_QUERY_URL, URL, rate_pair)
        if 'last' in result:
            logger.debug(f"Current rate of {symbol} is {result['last']}")
            return float(result['last'])
        else:
            logger.debug(f"Currency {symbol} isn't traded in GateIO")
            return -1.0

    def get_balance_in_dict(self):
        """
        :return: the account balance dictionary
        """
        # getting the account balance, the result is in string
        balance = self.gate_trade.balances()
        # converting the balance from str to dictionary
        balance = ast.literal_eval(balance)
        return balance

    def get_currency_balance(self, symbol="USDT"):
        """
        :param symbol: the symbol of the crypto currency
        :return: the account balance of specific cryptocurrency
        """
        balance = self.get_balance_in_dict()
        currency_balance = balance['available'][f'{symbol}']
        logger.debug(f'The currency balance of {symbol} is {currency_balance}')
        return float(currency_balance)

if  __name__ == '__main__':
    connection = GateClient()
    t = time.time()
    rate = (connection.get_rate('btc'))
    print(rate)
    t2 = time.time()
    print(t2-t)