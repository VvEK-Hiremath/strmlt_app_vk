import streamlit as st
import pandas as pd


def show_profile(kite):

    try:

        profile = kite.profile()

        st.write(
            f"Welcome, **{profile['user_name']}**"
        )

    except Exception as e:

        st.error(
            f"Could not load profile: {e}"
        )


def show_holdings(kite):

    st.divider()

    st.header("📊 Holdings")

    try:

        holdings = kite.mf_holdings()

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