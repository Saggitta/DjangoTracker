from .openexchange import OpenExchangeClient


APP_ID = "b6c0ee971d154d1fab1d2ac6993d5c7e"

client = OpenExchangeClient(APP_ID)


def exchange(amount, base="USD", to="UAH"):
    exchanged = client.convert(float(amount), base, to)
    return round(float(exchanged), 2)
