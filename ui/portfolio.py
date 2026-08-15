import streamlit as st
import pandas as pd

from kite.portfolio import (
    get_profile,
    get_equity_holdings,
    get_mutual_fund_holdings,
)


def show_profile(kite):

    try:
        profile = get_profile(kite)

        st.write(
            f"Welcome, **{profile['user_name']}**"
        )

    except Exception as e:

        st.error(
            f"Could not load profile: {e}"
        )


def show_equity_holdings(kite):

    st.divider()

    st.header("📈 Equity Holdings")

    try:

        holdings = get_equity_holdings(kite)

        if not holdings:

            st.info("No equity holdings found.")
            return

        df = pd.DataFrame(holdings)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )

    except Exception as e:

        st.error(
            f"Could not load equity holdings: {e}"
        )


def show_mutual_fund_holdings(kite):

    st.divider()

    st.header("🏦 Mutual Fund Holdings")

    try:

        holdings = get_mutual_fund_holdings(kite)

        if not holdings:

            st.info("No mutual fund holdings found.")
            return

        df = pd.DataFrame(holdings)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )

    except Exception as e:

        st.error(
            f"Could not load mutual fund holdings: {e}"
        )