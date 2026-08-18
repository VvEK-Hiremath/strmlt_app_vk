import streamlit as st
import pandas as pd

from kite.market_data import get_market_watch


def show_market_watch(kite):
    st.divider()
    st.header("📊 Market Watch")

    symbols = st.text_input("Symbols (comma separated)", value="INFY, TCS, RELIANCE")

    try:
        symbol_list = [item.strip() for item in symbols.split(",") if item.strip()]

        if not symbol_list:
            st.info("Enter at least one symbol to watch.")
            return

        quotes = get_market_watch(kite, symbol_list, exchange="NSE")

        if not quotes:
            st.info("No market data found for the entered symbols.")
            return

        df = pd.DataFrame(quotes)
        st.dataframe(df, use_container_width=True, hide_index=True)

    except Exception as e:
        st.error(f"Could not load market watch: {e}")
