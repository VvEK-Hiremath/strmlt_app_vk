import unittest

from kite.market_data import find_instrument, normalize_symbol


class MarketDataTests(unittest.TestCase):
    def test_normalize_symbol_uppercases_and_strips(self):
        self.assertEqual(normalize_symbol(" infy "), "INFY")

    def test_find_instrument_matches_exchange_and_symbol(self):
        instruments = [
            {"tradingsymbol": "INFY", "exchange": "NSE", "instrument_token": 256265},
            {"tradingsymbol": "TCS", "exchange": "NSE", "instrument_token": 2953217},
            {"tradingsymbol": "INFY", "exchange": "BSE", "instrument_token": 10789},
        ]

        instrument = find_instrument(instruments, "infy", "NSE")

        self.assertEqual(instrument["instrument_token"], 256265)


if __name__ == "__main__":
    unittest.main()
