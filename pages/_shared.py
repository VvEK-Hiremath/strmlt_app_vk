import streamlit as st

from kite.auth import get_access_token, handle_request_token, initialize_session, logout
from kite.client import create_kite_client, set_access_token


def initialize_kite_for_page(page_title, page_icon):
    st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide")
    st.title(page_title)

    initialize_session()
    kite = create_kite_client()

    if handle_request_token(kite):
        st.success("✅ Zerodha connected!")
        st.rerun()

    access_token = get_access_token()
    if not access_token:
        st.write("Connect your Zerodha account to continue.")
        login_url = kite.login_url()
        st.link_button("🔐 Login with Zerodha", login_url)
        st.stop()

    set_access_token(kite, access_token)
    st.success("🟢 Zerodha connected")
    return kite


def render_logout_button():
    st.divider()
    if st.button("Logout"):
        logout()
        st.rerun()
