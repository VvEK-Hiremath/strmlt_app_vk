import streamlit as st
import pandas as pd

from kite.portfolio import (
    calculate_portfolio_metrics,
    get_profile,
    get_equity_holdings,
    get_mutual_fund_holdings,
    get_positions,
    get_orders,
    get_funds,
)


def _currency(value):
    return f"₹{value:,.2f}"


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


def show_portfolio_summary(kite):

    st.divider()

    st.header("📊 Portfolio Summary")

    try:
        holdings = get_equity_holdings(kite)
        metrics = calculate_portfolio_metrics(holdings)

        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric("Total Investment", _currency(metrics["total_investment"]))
        col2.metric("Current Value", _currency(metrics["current_value"]))
        col3.metric("Overall P&L", _currency(metrics["overall_pnl"]))
        col4.metric("P&L %", f"{metrics['pnl_percent']:.2f}%")

        today_pnl = 0.0
        for holding in holdings or []:
            today_pnl += float(holding.get("day_change", 0) or 0)
        col5.metric("Today's P&L", _currency(today_pnl))

        st.caption("Summary based on equity holdings")

    except Exception as e:
        st.error(f"Could not load portfolio summary: {e}")


def show_positions(kite):

    st.divider()
    st.header("📍 Positions")

    try:
        positions = get_positions(kite)

        if not positions:
            st.info("No open positions found.")
            return

        df = pd.DataFrame(positions)
        display_columns = [
            col for col in [
                "tradingsymbol",
                "exchange",
                "quantity",
                "average_price",
                "last_price",
                "pnl",
                "product",
            ] if col in df.columns
        ]

        if display_columns:
            st.dataframe(df[display_columns], use_container_width=True, hide_index=True)
        else:
            st.dataframe(df, use_container_width=True, hide_index=True)

    except Exception as e:
        st.error(f"Could not load positions: {e}")


def show_orders(kite):

    st.divider()
    st.header("🧾 Orders")

    try:
        orders = get_orders(kite)

        if not orders:
            st.info("No orders found.")
            return

        df = pd.DataFrame(orders)
        st.dataframe(df, use_container_width=True, hide_index=True)

    except Exception as e:
        st.error(f"Could not load orders: {e}")


def show_funds(kite):

    st.divider()
    st.header("💰 Funds / Margins")

    try:
        margins = get_funds(kite)
        equity = margins.get("equity", {}) if isinstance(margins, dict) else {}

        if not equity:
            st.info("No margin data found.")
            return

        metric_cols = st.columns(4)
        values = [
            ("Available Cash", equity.get("available_cash", equity.get("availablecash", 0))),
            ("Used Margin", equity.get("utiliseddebits", equity.get("used_margin", 0))),
            ("Opening Balance", equity.get("opening_balance", 0)),
            ("Net", equity.get("net", 0)),
        ]

        for idx, (label, value) in enumerate(values):
            metric_cols[idx].metric(label, _currency(float(value or 0)))

    except Exception as e:
        st.error(f"Could not load funds: {e}")


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