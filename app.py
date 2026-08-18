import streamlit as st

st.set_page_config(
    page_title="Zerodha Dashboard",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Zerodha Dashboard")

st.write("Choose a page from the sidebar to view either your portfolio or market data.")

st.info("Portfolio page: holdings, positions, orders, funds, and summary")
st.info("Market Data page: live watchlist and quote-driven analysis")
