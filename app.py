import streamlit as st

from kite.client import create_kite_client, set_access_token
from kite.auth import (
    initialize_session,
    handle_request_token,
    get_access_token,
    logout,
)
from pages.portfolio import (
    show_profile,
    show_equity_holdings,
    show_mutual_fund_holdings,
)


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="My Zerodha Portfolio",
    page_icon="📈",
    layout="wide",
)

st.title("📈 My Zerodha Portfolio")


# --------------------------------------------------
# INITIALIZE
# --------------------------------------------------

initialize_session()

kite = create_kite_client()


# --------------------------------------------------
# HANDLE ZERODHA CALLBACK
# --------------------------------------------------

if handle_request_token(kite):

    st.success("✅ Zerodha connected!")

    st.rerun()


# --------------------------------------------------
# LOGIN
# --------------------------------------------------

access_token = get_access_token()

if not access_token:

    st.write(
        "Connect your Zerodha account to continue."
    )

    login_url = kite.login_url()

    st.link_button(
        "🔐 Login with Zerodha",
        login_url,
    )

    st.stop()


# --------------------------------------------------
# CONNECTED
# --------------------------------------------------

set_access_token(
    kite,
    access_token,
)

st.success("🟢 Zerodha connected")


# --------------------------------------------------
# PORTFOLIO
# --------------------------------------------------

show_profile(kite)

show_equity_holdings(kite)

show_mutual_fund_holdings(kite)


# --------------------------------------------------
# LOGOUT
# --------------------------------------------------

st.divider()

if st.button("Logout"):

    logout()

    st.rerun()