import streamlit as st

from config import API_SECRET


def initialize_session():
    if "access_token" not in st.session_state:
        st.session_state.access_token = None


def get_access_token():
    return st.session_state.access_token


def handle_request_token(kite):
    request_token = st.query_params.get("request_token")

    if not request_token:
        return False

    if st.session_state.access_token:
        return False

    try:
        session_data = kite.generate_session(
            request_token,
            api_secret=API_SECRET,
        )

        st.session_state.access_token = session_data["access_token"]

        # Remove request token from URL
        st.query_params.clear()

        return True

    except Exception as e:
        st.error(
            f"❌ Could not create Kite session: {e}"
        )

        return False


def logout():
    st.session_state.access_token = None
    st.query_params.clear()