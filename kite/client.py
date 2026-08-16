from kiteconnect import KiteConnect

from config import API_KEY


def create_kite_client():
    return KiteConnect(api_key=API_KEY)


def set_access_token(kite, access_token):
    kite.set_access_token(access_token)

    return kite