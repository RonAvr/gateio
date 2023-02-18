from ..managers.Extractor import Extractor
import unittest


class ExtractorTest(unittest.TestCase):

    def test_Simple_Contracts(self):
        req: str = "Binance Futures Will Launch USDⓈ-M ASTR Perpetual Contracts with Up to 20X Leverage"
        extractor: Extractor = Extractor()
        res: str = extractor.get_symbol(announcement=req)
        self.assertEqual("ASTR", res)

    def test_Pair_Contracts(self):
        req: str = "Binance Futures Will Launch USDⓈ-M MINA and HIGH Perpetual Contracts with Up to 20X Leverage"
        extractor: Extractor = Extractor()
        res: str = extractor.get_symbol(announcement=req)
        self.assertEqual("MINA", res)

    def test_Symbol_Contracts(self):
        req: str = "Binance Futures Will Launch USDⓈ-M Threshold (T) Perpetual Contracts with Up to 20X Leverage"
        extractor: Extractor = Extractor()
        res: str = extractor.get_symbol(announcement=req)
        self.assertEqual("T", res)

    def test_Pair_and_Symbol_Contracts(self):
        req: str = "Binance Futures Will Launch USDⓈ-M Threshold (THR) and HIGH Perpetual Contracts with Up to 20X Leverage"
        extractor: Extractor = Extractor()
        res: str = extractor.get_symbol(announcement=req)
        self.assertEqual("THR", res)

    def test_Two_Pairs_Trading_Pair(self):
        req: str = "Binance Adds FET/TRY & PROS/USDT Trading Pairs"
        extractor: Extractor = Extractor()
        res: str = extractor.get_symbol(announcement=req)
        self.assertEqual("PROS", res)

    def test_Many_Pair_Trading_Pair(self):
        req: str = "Binance Adds ARPA/ETH, PHB/USDT & VITE/BUSD Trading Pairs"
        extractor: Extractor = Extractor()
        res: str = extractor.get_symbol(announcement=req)
        self.assertEqual("PHB", res)

    def test_Simple_Listing(self):
        req: str = "Binance Will List Optimism (OP)"
        extractor: Extractor = Extractor()
        res: str = extractor.get_symbol(announcement=req)
        self.assertEqual("OP", res)

    def test_Many_Listing(self):
        req: str = "Binance Will List MobileCoin (MOB) and Nexo (NEXO)"
        extractor: Extractor = Extractor()
        res: str = extractor.get_symbol(announcement=req)
        self.assertEqual("MOB", res)

    def test_Simple_Innovation_Listing(self):
        req: str = "Binance Will List GMX (GMX) in the Innovation Zone"
        extractor: Extractor = Extractor()
        res: str = extractor.get_symbol(announcement=req)
        self.assertEqual("", res)

    # def test_c(self):
    #     extractor: Extractor = Extractor()
    #     res: str = extractor.extract_annoncement()
    #     pass

