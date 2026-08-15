def get_equity_holdings(kite):
    return kite.holdings()


def get_mutual_fund_holdings(kite):
    return kite.mf_holdings()


def get_profile(kite):
    return kite.profile()