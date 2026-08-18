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

    quote = kite.quote(instrument["exchange"], str(instrument["instrument_token"]))
    return quote


def get_historical_data(kite, symbol, interval="day", from_date=None, to_date=None, exchange="NSE"):
    instruments = kite.instruments(exchange=exchange)
    instrument = find_instrument(instruments, symbol, exchange)

    if instrument is None:
        raise ValueError(f"Instrument not found for {symbol} on {exchange}")

    if from_date is None or to_date is None:
        return kite.historical_data(
            instrument_token=instrument["instrument_token"],
            from_date=from_date,
            to_date=to_date,
            interval=interval,
        )

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

        quote = kite.quote(instrument["exchange"], str(instrument["instrument_token"]))
        quote_data = next(iter(quote.values()), {}) if isinstance(quote, dict) else {}

        watchlist.append({
            "symbol": instrument["tradingsymbol"],
            "instrument_token": instrument["instrument_token"],
            "last_price": quote_data.get("last_price", 0),
            "change": quote_data.get("net_change", 0),
            "percentage_change": quote_data.get("p_change", 0),
            "exchange": exchange,
        })

    return watchlist
