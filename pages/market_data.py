import streamlit as st

from pages._shared import initialize_kite_for_page
from ui.market_data import show_market_watch


kite = initialize_kite_for_page("Market Data", "📈")
show_market_watch(kite)
