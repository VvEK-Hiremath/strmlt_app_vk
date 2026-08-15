import streamlit as st
from kiteconnect import KiteConnect

st.set_page_config(
    page_title="My Zerodha Portfolio",
    page_icon="📈"
)

st.title("📈 My Zerodha Portfolio")

# Load credentials from Streamlit Secrets
API_KEY = st.secrets["KITE_API_KEY"]

kite = KiteConnect(api_key=API_KEY)

st.write("Streamlit is working ✅")

login_url = kite.login_url()

st.link_button(
    "🔐 Login with Zerodha",
    login_url
)
