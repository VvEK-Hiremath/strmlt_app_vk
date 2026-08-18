def normalize_symbol(symbol):
    return (symbol or "").strip().upper()


def find_instrument(instruments, symbol, exchange="NSE"):
    normalized_symbol = normalize_symbol(symbol)

    for instrument in instruments or []:
        if instrument.get("tradingsymbol", "").upper() == normalized_symbol and instrument.get("exchange", "").upper() == exchange.upper():
            return instrument

    return None


def get_quote(kite, symbol, exchange="NSE"):
    instruments = kite.instruments(exchange=exchange)
    instrument = find_instrument(instruments, symbol, exchange)

    if instrument is None:
        raise ValueError(f"Instrument not found for {symbol} on {exchange}")

    token = str(instrument["instrument_token"])
    quote = kite.quote(token)

    if isinstance(quote, dict):
        return quote.get(token, quote.get(int(token), {}))

    if isinstance(quote, list) and quote:
        return quote[0]

    return {}


def get_historical_data(kite, symbol, interval="day", from_date=None, to_date=None, exchange="NSE"):
    instruments = kite.instruments(exchange=exchange)
    instrument = find_instrument(instruments, symbol, exchange)

    if instrument is None:
        raise ValueError(f"Instrument not found for {symbol} on {exchange}")

    return kite.historical_data(
        instrument_token=instrument["instrument_token"],
        from_date=from_date,
        to_date=to_date,
        interval=interval,
    )


def get_market_watch(kite, symbols, exchange="NSE"):
    instruments = kite.instruments(exchange=exchange)
    watchlist = []

    for symbol in symbols or []:
        instrument = find_instrument(instruments, symbol, exchange)
        if instrument is None:
            continue

        token = str(instrument["instrument_token"])
        quote_response = kite.quote(token)

        if isinstance(quote_response, dict):
            quote_data = quote_response.get(token, quote_response.get(int(token), {}))
        elif isinstance(quote_response, list) and quote_response:
            quote_data = quote_response[0]
        else:
            quote_data = {}

        watchlist.append({
            "symbol": instrument["tradingsymbol"],
            "instrument_token": instrument["instrument_token"],
            "last_price": quote_data.get("last_price", 0),
            "change": quote_data.get("net_change", 0),
            "percentage_change": quote_data.get("p_change", 0),
            "exchange": exchange,
        })

    return watchlist
