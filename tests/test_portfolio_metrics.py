import unittest

from kite.portfolio import calculate_portfolio_metrics


class PortfolioMetricsTests(unittest.TestCase):
    def test_calculate_portfolio_metrics_from_holdings(self):
        holdings = [
            {"tradingsymbol": "INFY", "quantity": 20, "average_price": 1400, "last_price": 1500},
            {"tradingsymbol": "TCS", "quantity": 10, "average_price": 3200, "last_price": 3500},
        ]

        metrics = calculate_portfolio_metrics(holdings)

        self.assertAlmostEqual(metrics["total_investment"], 60000.0)
        self.assertAlmostEqual(metrics["current_value"], 65000.0)
        self.assertAlmostEqual(metrics["overall_pnl"], 5000.0)
        self.assertAlmostEqual(metrics["pnl_percent"], 8.333333333333334)


if __name__ == "__main__":
    unittest.main()
