import unittest

from kite.market_data import find_instrument, normalize_symbol, get_market_watch


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

    def test_get_market_watch_uses_instrument_token_quote_format(self):
        class FakeKite:
            def instruments(self, exchange="NSE"):
                return [
                    {"tradingsymbol": "INFY", "exchange": "NSE", "instrument_token": 256265},
                ]

            def quote(self, instrument_token):
                return {"256265": {"last_price": 1500, "net_change": 25, "p_change": 1.7}}

        watchlist = get_market_watch(FakeKite(), ["infy"])

        self.assertEqual(watchlist[0]["symbol"], "INFY")
        self.assertEqual(watchlist[0]["last_price"], 1500)


if __name__ == "__main__":
    unittest.main()
