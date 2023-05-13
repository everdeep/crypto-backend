from api.service import ExchangeService
from config import Config

import pytest


@pytest.fixture
def api_keys():
    api_keys = {
        "binance": {"api_key": Config().BINANCE_API_KEY, "api_secret": Config().BINANCE_API_SECRET},
        "bittrex": {"api_key": Config().BITTREX_API_KEY, "api_secret": Config().BITTREX_API_SECRET},
    }

    yield api_keys


def test_get_binance_exchange(api_keys):
    exchange = ExchangeService().get_exchange("Binance", **api_keys["binance"])
    assert exchange is not None


def test_get_bittrex_exchange(api_keys):
    exchange = ExchangeService().get_exchange("Bittrex", **api_keys["bittrex"])
    assert exchange is not None


def test_get_exchange_invalid_exchange(api_keys):
    with pytest.raises(ValueError):
        ExchangeService().get_exchange("invalid_exchange", **api_keys["binance"])
