import streamlit as st
import pandas as pd
from kiteconnect import KiteConnect

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
# SECRETS
# --------------------------------------------------

API_KEY = st.secrets["KITE_API_KEY"]
API_SECRET = st.secrets["KITE_API_SECRET"]

# --------------------------------------------------
# KITE CLIENT
# --------------------------------------------------

kite = KiteConnect(api_key=API_KEY)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "access_token" not in st.session_state:
    st.session_state.access_token = None


# --------------------------------------------------
# HANDLE ZERODHA REDIRECT
# --------------------------------------------------

query_params = st.query_params

request_token = query_params.get("request_token")

if request_token and not st.session_state.access_token:

    try:
        session_data = kite.generate_session(
            request_token,
            api_secret=API_SECRET,
        )

        st.session_state.access_token = session_data["access_token"]

        # Remove request_token from browser URL
        st.query_params.clear()

        st.success("✅ Zerodha connected successfully!")

        st.rerun()

    except Exception as e:
        st.error(f"❌ Zerodha authentication failed: {e}")


# --------------------------------------------------
# LOGIN SCREEN
# --------------------------------------------------

if not st.session_state.access_token:

    st.subheader("Connect your Zerodha account")

    login_url = kite.login_url()

    st.markdown(
        f"""
        <a href="{login_url}" target="_self">
            <button style="
                background-color:#387ed1;
                color:white;
                padding:12px 24px;
                border:none;
                border-radius:6px;
                font-size:16px;
                cursor:pointer;
            ">
                🔐 Login with Zerodha
            </button>
        </a>
        """,
        unsafe_allow_html=True,
    )

    st.info(
        "Click the button above and complete your Zerodha login."
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
# FETCH PROFILE
# --------------------------------------------------

try:

    profile = kite.profile()

    user_name = profile.get("user_name", "")
    user_id = profile.get("user_id", "")

    st.write(
        f"Welcome, **{user_name}** (`{user_id}`)"
    )

except Exception as e:

    st.error(
        f"Could not retrieve Zerodha profile: {e}"
    )


# --------------------------------------------------
# HOLDINGS
# --------------------------------------------------

st.divider()

st.header("📊 My Holdings")

if st.button("🔄 Refresh Holdings"):

    try:

        holdings = kite.holdings()

        if not holdings:

            st.info("You currently have no holdings.")

        else:

            df = pd.DataFrame(holdings)

            # --------------------------------------
            # PORTFOLIO CALCULATIONS
            # --------------------------------------

            total_investment = (
                df["average_price"] * df["quantity"]
            ).sum()

            current_value = (
                df["last_price"] * df["quantity"]
            ).sum()

            total_pnl = (
                df["pnl"]
            ).sum()

            pnl_percent = (
                (total_pnl / total_investment) * 100
                if total_investment
                else 0
            )

            # --------------------------------------
            # SUMMARY
            # --------------------------------------

            col1, col2, col3, col4 = st.columns(4)

            col1.metric(
                "Investment",
                f"₹{total_investment:,.2f}",
            )

            col2.metric(
                "Current Value",
                f"₹{current_value:,.2f}",
            )

            col3.metric(
                "Total P&L",
                f"₹{total_pnl:,.2f}",
            )

            col4.metric(
                "P&L %",
                f"{pnl_percent:.2f}%",
            )

            # --------------------------------------
            # TABLE
            # --------------------------------------

            st.subheader("Holdings")

            display_columns = [
                "tradingsymbol",
                "exchange",
                "quantity",
                "average_price",
                "last_price",
                "pnl",
            ]

            available_columns = [
                column
                for column in display_columns
                if column in df.columns
            ]

            st.dataframe(
                df[available_columns],
                use_container_width=True,
                hide_index=True,
            )

    except Exception as e:

        st.error(
            f"❌ Could not fetch holdings: {e}"
        )


# --------------------------------------------------
# LOGOUT
# --------------------------------------------------

st.divider()

if st.button("Logout"):

    st.session_state.access_token = None

    st.query_params.clear()

    st.rerun()