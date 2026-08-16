# ZERODHA PORTFOLIO & ALGO TRADING PLATFORM

## Project Goal

Build a personal Streamlit web application connected to Zerodha Kite Connect.

Start with:
- Portfolio monitoring

Eventually reach:
- Strategy development
- Backtesting
- Paper trading
- Risk management
- Live algo trading

## Current Status

- [✓] GitHub repository
- [✓] Streamlit Cloud deployment
- [✓] Streamlit Secrets
- [✓] Kite Connect authentication
- [✓] Request token → access token
- [✓] Modular code structure
- [✓] Zerodha profile
- [✓] Mutual fund holdings
- [✓] Basic portfolio UI

## High-Level Architecture

```text
                    STREAMLIT APP
                         |
             +-----------+-----------+
             |                       |
             v                       v
         PORTFOLIO                 TRADING
             |                       |
       +-----+-----+          +------+------+ 
       |     |     |          |             |
     Equity  MF  Positions   Strategy      Risk
                               |
                               v
                            Signal
                               |
                               v
                          +----+----+
                          |         |
                          v         v
                     Backtest    Execution
                                    |
                              +-----+-----+
                              |           |
                              v           v
                            Paper       Live
                                         |
                                         v
                                    Kite Connect
```

## Target Project Structure

strmlt_app_vk/
|
+-- app.py
+-- config.py
|
+-- kite/
|   +-- **init**.py
|   +-- client.py
|   +-- auth.py
|   +-- portfolio.py
|   +-- market_data.py
|   +-- orders.py
|   +-- positions.py
|   +-- funds.py
|
+-- data/
|   +-- market.py
|   +-- historical.py
|   +-- storage.py
|
+-- strategy/
|   +-- **init**.py
|   +-- base.py
|   +-- moving_average.py
|   +-- rsi.py
|   +-- breakout.py
|
+-- risk/
|   +-- **init**.py
|   +-- manager.py
|   +-- rules.py
|
+-- execution/
|   +-- **init**.py
|   +-- paper.py
|   +-- live.py
|
+-- ui/
|   +-- **init**.py
|   +-- portfolio.py
|   +-- charts.py
|   +-- trading.py
|
+-- requirements.txt
+-- .gitignore

## DESIGN PRINCIPLE

Keep these responsibilities separate:

```
UI
  |
  v
Business Logic
  |
  v
Data / API
  |
  v
Zerodha / Storage
```

Do NOT allow:

```
Streamlit UI
    |
    +---- directly places orders
    |
    +---- directly implements strategy
    |
    +---- directly handles risk
```

Instead:

```
UI
  |
  v
Strategy
  |
  v
Risk Engine
  |
  v
Order Manager
  |
  v
Broker
```

# PHASE 1 — PORTFOLIO FOUNDATION

Goal:
Build a reliable portfolio dashboard.

Features:

[✓] Zerodha authentication
[✓] User profile
[✓] Mutual fund holdings
[ ] Equity holdings
[ ] Positions
[ ] Orders
[ ] Funds / margins
[ ] Total investment
[ ] Current portfolio value
[ ] Overall P&L
[ ] Today's P&L
[ ] Portfolio allocation
[ ] Individual stock details

Target UI:

```
+----------------------------------------------+
| My Zerodha Portfolio             CONNECTED   |
+----------------------------------------------+
| Investment | Current Value | P&L | P&L %     |
+----------------------------------------------+
| Equity Holdings                              |
|                                              |
| Symbol | Qty | Avg | LTP | Investment | P&L |
+----------------------------------------------+
| Mutual Fund Holdings                         |
+----------------------------------------------+
```

# PHASE 2 — MARKET DATA LAYER

Goal:
Create a clean data layer independent of the UI.

Architecture:

```
Zerodha Kite
     |
     v
market_data.py
     |
     v
data layer
     |
     +---- Live prices
     +---- Historical candles
     +---- OHLC
     +---- Volume
     +---- Instruments
```

Example:

```
prices = get_market_data(
    symbol="INFY"
)
```

The UI should NOT need to know how Kite provides the data.

Features:

[ ] Live quotes
[ ] OHLC data
[ ] Historical candles
[ ] Multiple timeframes
[ ] Instrument lookup
[ ] Market watch
[ ] Data caching
[ ] Local data storage if required

# PHASE 3 — CHARTS & ANALYSIS

Goal:
Visualize market and portfolio data.

Features:

[ ] Candlestick charts
[ ] Volume
[ ] Moving averages
[ ] RSI
[ ] MACD
[ ] Support/resistance
[ ] Portfolio performance
[ ] Stock performance
[ ] Drawdown chart

Example:

```
INFY

Price
  |
  |        /\       /\
  |   /\  /  \  /\ /  \
  |__/  \/    \/  V    \__
  |
  +--------------------------> Time

Indicators:
    MA20
    MA50
    RSI
```

# PHASE 4 — STRATEGY ENGINE

Goal:
Create reusable trading strategies.

Architecture:

```
Market Data
     |
     v
  Strategy
     |
     v
   Signal
```

A strategy should produce:

```
BUY
SELL
HOLD
```

Example:

```
data
  |
  v
Moving Average Strategy
  |
  +---- BUY
  +---- SELL
  +---- HOLD
```

Potential strategies:

[ ] Moving average crossover
[ ] RSI strategy
[ ] Breakout strategy
[ ] Momentum strategy
[ ] Mean reversion
[ ] Custom personal strategies

IMPORTANT:

Strategy logic should NOT directly place real orders.

# PHASE 5 — BACKTESTING ENGINE

Goal:
Test strategies against historical data before trading real money.

Architecture:

```
Historical Data
      |
      v
   Strategy
      |
      v
  Signal
      |
      v
Simulated Order
      |
      v
Portfolio Simulator
      |
      v
 Performance
```

Example result:

```
Strategy: Moving Average Crossover

Initial Capital:     ₹1,00,000
Final Capital:       ₹1,42,500
Return:                 +42.5%
Max Drawdown:           -12.3%
Number of Trades:          87
Win Rate:                 54%
Profit Factor:            1.62
```

Metrics to track:

[ ] Total return
[ ] CAGR
[ ] Maximum drawdown
[ ] Win rate
[ ] Average win
[ ] Average loss
[ ] Profit factor
[ ] Number of trades
[ ] Sharpe ratio
[ ] Transaction costs
[ ] Slippage

IMPORTANT:

Do not judge a strategy only by historical return.

Include:
Brokerage
Taxes/charges
Slippage
Liquidity
Drawdown
Overfitting

# PHASE 6 — PAPER TRADING

Goal:
Run strategies using simulated money.

Architecture:

```
Live Market Data
      |
      v
   Strategy
      |
      v
    Signal
      |
      v
  Risk Engine
      |
      v
 Paper Broker
      |
      v
 Simulated P&L
```

Example:

```
BUY INFY

Entry:       ₹1,520
Quantity:       10
Stop Loss:   ₹1,490
Target:      ₹1,580

Result:
    +₹600
```

Features:

[ ] Virtual account balance
[ ] Virtual positions
[ ] Virtual orders
[ ] Simulated fills
[ ] P&L
[ ] Trade history
[ ] Strategy performance
[ ] Slippage simulation
[ ] Brokerage simulation

# PHASE 7 — RISK ENGINE

Goal:
Prevent strategies from taking unacceptable risk.

Architecture:

```
Strategy Signal
      |
      v
  Risk Engine
      |
   +--+--+
   |     |
Reject  Approve
         |
         v
   Order Manager
```

Risk controls:

[ ] Maximum capital per trade
[ ] Maximum position size
[ ] Maximum number of positions
[ ] Maximum daily loss
[ ] Maximum portfolio exposure
[ ] Stop loss
[ ] Maximum order value
[ ] Trading hours
[ ] Duplicate order protection
[ ] Circuit breaker
[ ] Emergency kill switch

Example:

```
Strategy:
    BUY INFY

Risk Engine checks:

    Capital available?
    Position limit okay?
    Daily loss limit okay?
    Market open?
    Existing order?
    Existing position?
    Maximum exposure okay?

        |
        v

    APPROVED / REJECTED
```

# PHASE 8 — ORDER MANAGEMENT

Goal:
Create a controlled interface for placing orders.

Architecture:

```
Strategy
   |
   v
Risk Engine
   |
   v
Order Manager
   |
   +----------+
   |          |
   v          v
Paper       Live
Broker      Broker
               |
               v
           Zerodha
```

Order Manager responsibilities:

[ ] Create orders
[ ] Validate orders
[ ] Track order status
[ ] Handle rejected orders
[ ] Handle partial fills
[ ] Prevent duplicate orders
[ ] Maintain order history
[ ] Reconcile positions

# PHASE 9 — LIVE TRADING

Goal:
Allow approved strategies to place real Zerodha orders.

Architecture:

```
Market Data
     |
     v
  Strategy
     |
     v
  Signal
     |
     v
 Risk Engine
     |
     v
Order Manager
     |
     v
Live Execution
     |
     v
Kite Connect
     |
     v
Zerodha
```

## LIVE TRADING SAFETY

Before enabling live orders:

[ ] Backtest completed
[ ] Paper trading completed
[ ] Strategy validated
[ ] Risk limits implemented
[ ] Position reconciliation implemented
[ ] Duplicate order protection
[ ] Error handling
[ ] Network failure handling
[ ] API failure handling
[ ] Emergency stop
[ ] Daily loss limit
[ ] Maximum order value
[ ] Manual override
[ ] Trading logs
[ ] Alerts / notifications

## LIVE MODE SHOULD BE EXPLICIT

The application should clearly show:

```
🟢 PAPER TRADING
```

or

```
🔴 LIVE TRADING
```

Never make live trading the default.

# PHASE 10 — MONITORING & OPERATIONS

Goal:
Make the algo reliable when running unattended.

Features:

[ ] Application logs
[ ] Trade logs
[ ] Strategy logs
[ ] Error logs
[ ] API health monitoring
[ ] Order monitoring
[ ] Position reconciliation
[ ] Daily P&L monitoring
[ ] Alerts
[ ] Kill switch
[ ] System health dashboard

Possible alerts:

```
Strategy started
Strategy stopped
Order placed
Order rejected
Stop loss triggered
Daily loss limit reached
API disconnected
Unexpected position detected
```

# FINAL SYSTEM ARCHITECTURE

```
                     STREAMLIT UI
                          |
         +----------------+----------------+
         |                                 |
    PORTFOLIO UI                       TRADING UI
         |                                 |
         v                                 v
   Portfolio Service                 Strategy Engine
         |                                 |
         v                                 v
    Data Layer                      Risk Engine
         |                                 |
         |                                 v
         |                           Order Manager
         |                                 |
         +----------------+----------------+
                          |
                          v
                   Execution Layer
                     /         \
                    /           \
                   v             v
             Paper Broker    Live Broker
                                 |
                                 v
                            Kite Connect
                                 |
                                 v
                              Zerodha
```

# DEVELOPMENT ORDER

Do NOT build everything at once.

Recommended sequence:

```
1.  Equity holdings
2.  Positions
3.  Orders
4.  Funds / margins
5.  Portfolio calculations
6.  Market quotes
7.  Historical data
8.  Charts
9.  Strategy framework
10. First simple strategy
11. Backtesting
12. Paper trading
13. Risk engine
14. Order management
15. Live execution
16. Monitoring / alerts
```

# CURRENT NEXT STEP

Current application:

```
Streamlit
   |
   +-- Kite authentication
   |
   +-- Profile
   |
   +-- Mutual fund holdings
   |
   +-- Modular structure
```

NEXT FEATURE:

```
Add Equity Holdings
```

Then:

```
Equity Holdings
     +
Mutual Funds
     +
Positions
     +
Orders
     +
Funds
     |
     v
Portfolio Dashboard
```

# LONG-TERM GOAL

Build a personal trading platform where:

```
I can see my portfolio
         ↓
I can analyze markets
         ↓
I can create strategies
         ↓
I can backtest strategies
         ↓
I can paper trade strategies
         ↓
I can apply risk controls
         ↓
I can optionally enable live trading
         ↓
Zerodha executes approved orders
```

# CORE PRINCIPLE

```
DATA
  ↓
STRATEGY
  ↓
SIGNAL
  ↓
RISK
  ↓
EXECUTION
  ↓
BROKER
```

Never skip the RISK layer before LIVE execution.