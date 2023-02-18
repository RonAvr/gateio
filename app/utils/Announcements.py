from enum import Enum


class Announcements(str, Enum):
    contract = "Perpetual Contracts with Up to 20X Leverage"
    trading_pairs = "Trading Pairs"
    trading_pair = "Trading Pair"
    binance_adds = "Binance Adds"
    binance_will_list = "Binance Will List"
    usd = "USDⓈ-M"
    usdt = "USDT"
    innovation_zone = "Innovation Zone"