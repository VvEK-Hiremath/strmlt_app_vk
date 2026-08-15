import streamlit as st
from kiteconnect import KiteConnect
import pandas as pd

st.set_page_config(
    page_title="My Zerodha Portfolio",
    page_icon="📈",
    layout="wide",
)

st.title("📈 My Zerodha Portfolio")

# --------------------------------------------------
# CONFIG
# --------------------------------------------------

API_KEY = st.secrets["KITE_API_KEY"]
API_SECRET = st.secrets["KITE_API_SECRET"]

kite = KiteConnect(api_key=API_KEY)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "access_token" not in st.session_state:
    st.session_state.access_token = None


# --------------------------------------------------
# GET REQUEST TOKEN FROM URL
# --------------------------------------------------

request_token = st.query_params.get("request_token")


# --------------------------------------------------
# EXCHANGE REQUEST TOKEN → ACCESS TOKEN
# --------------------------------------------------

if request_token and not st.session_state.access_token:

    try:

        session_data = kite.generate_session(
            request_token,
            api_secret=API_SECRET,
        )

        st.session_state.access_token = session_data["access_token"]

        # Remove request_token from browser URL
        st.query_params.clear()

        st.success("✅ Zerodha connected!")

        st.rerun()

    except Exception as e:

        st.error(
            f"❌ Could not create Kite session: {e}"
        )


# --------------------------------------------------
# NOT CONNECTED
# --------------------------------------------------

if not st.session_state.access_token:

    st.write("Connect your Zerodha account to continue.")

    login_url = kite.login_url()

    st.link_button(
        "🔐 Login with Zerodha",
        login_url,
    )

    st.stop()


# --------------------------------------------------
# CONNECTED
# --------------------------------------------------

kite.set_access_token(
    st.session_state.access_token
)

st.success("🟢 Zerodha connected")


# --------------------------------------------------
# PROFILE
# --------------------------------------------------

try:

    profile = kite.profile()

    st.write(
        f"Welcome, **{profile['user_name']}**"
    )

except Exception as e:

    st.error(
        f"Could not load profile: {e}"
    )


# --------------------------------------------------
# HOLDINGS
# --------------------------------------------------

st.divider()

st.header("📊 Holdings")

try:

    holdings = kite.holdings()

    if not holdings:

        st.info("No holdings found.")

    else:

        df = pd.DataFrame(holdings)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
        )

except Exception as e:

    st.error(
        f"Could not load holdings: {e}"
    )


# --------------------------------------------------
# LOGOUT
# --------------------------------------------------

st.divider()

if st.button("Logout"):

    st.session_state.access_token = None

    st.query_params.clear()

    st.rerun()
