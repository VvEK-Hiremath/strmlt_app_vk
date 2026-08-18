def _to_float(value, default=0.0):
    try:
        if value is None:
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def calculate_portfolio_metrics(holdings):
    total_investment = 0.0
    current_value = 0.0

    for holding in holdings or []:
        quantity = _to_float(holding.get("quantity"))
        average_price = _to_float(holding.get("average_price"))
        last_price = _to_float(holding.get("last_price"))

        total_investment += quantity * average_price
        current_value += quantity * last_price

    overall_pnl = current_value - total_investment
    pnl_percent = (overall_pnl / total_investment * 100) if total_investment else 0.0

    return {
        "total_investment": total_investment,
        "current_value": current_value,
        "overall_pnl": overall_pnl,
        "pnl_percent": pnl_percent,
    }


def get_equity_holdings(kite):
    return kite.holdings()


def get_mutual_fund_holdings(kite):
    return kite.mf_holdings()


def get_positions(kite):
    positions = kite.positions()

    if isinstance(positions, dict):
        return positions.get("net", [])

    return positions or []


def get_orders(kite):
    return kite.orders() or []


def get_funds(kite):
    try:
        return kite.margins() or {}
    except Exception:
        return {}


def get_profile(kite):
    return kite.profile()