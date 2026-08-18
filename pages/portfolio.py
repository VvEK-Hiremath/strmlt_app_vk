import streamlit as st

from pages._shared import initialize_kite_for_page, render_logout_button
from ui.portfolio import (
    show_profile,
    show_portfolio_summary,
    show_positions,
    show_orders,
    show_funds,
    show_equity_holdings,
    show_mutual_fund_holdings,
)


kite = initialize_kite_for_page("Portfolio", "📊")

show_profile(kite)
show_portfolio_summary(kite)
show_positions(kite)
show_orders(kite)
show_funds(kite)
show_equity_holdings(kite)
show_mutual_fund_holdings(kite)

render_logout_button()
