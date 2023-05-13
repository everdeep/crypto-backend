from http import HTTPStatus
from flask import Blueprint, jsonify, request
from flasgger import swag_from
from flask_login import login_required, current_user

from api.schema import (
    SymbolSchema,
    CurrencyPairConfigSchema,
    OrderSchema,
    PortfolioSchema,
)
from api.service import DataService

from app import db

data_api = Blueprint("api", __name__)


@data_api.route("/symbols", methods=["GET"])
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Returns a list of symbols",
                "schema": SymbolSchema,
            }
        }
    }
)
def getSymbols():
    """
    Return a list of symbols
    ---
    """
    result = DataService().get_symbols()
    return jsonify([symbol.symbol for symbol in result]), 200


@data_api.route("/symbols/<symbol>", methods=["GET"])
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Returns a list of symbols and its associated currency pairs",
                "schema": SymbolSchema,
            }
        }
    }
)
def getSymbol(symbol):
    """
    Returns the symbol and its associated currency pairs
    ---
    """
    result = DataService().get_symbol(symbol)
    return SymbolSchema().dump(result), 200


@data_api.route("/config", methods=["GET"])
@login_required
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Returns a list of currency pair configs for a user",
                "schema": CurrencyPairConfigSchema,
            }
        }
    }
)
def geCurrencyPairConfigs():
    """
    Returns the currency pair config of the user
    ---
    """
    args = request.args

    result = DataService().get_currency_pair_configs(current_user.id, args)
    return CurrencyPairConfigSchema().dump(result, many=True), 200


@data_api.route("/config/<currency_pair>", methods=["GET"])
@login_required
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Returns a config of a currency pair",
                "schema": CurrencyPairConfigSchema,
            }
        }
    }
)
def getCurrencyPairConfig(currency_pair):
    """
    Returns the currency pair config of the user
    ---
    """
    result = DataService().get_currency_pair_config(current_user.id, currency_pair)
    return CurrencyPairConfigSchema().dump(result), 200


@data_api.route("/config/<currency_pair>", methods=["POST"])
@login_required
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Updaets the config of a currency pair",
                "schema": CurrencyPairConfigSchema,
            }
        }
    }
)
def updateCurrencyPairConfig(currency_pair):
    """
    Updates the config of a currency pair
    ---
    """
    request_data = request.get_json()
    result = DataService().update_currency_pair_config(
        currency_pair, current_user.id, request_data
    )
    return CurrencyPairConfigSchema().dump(result), 200


# Get orders for a user
@data_api.route("/orders", methods=["GET"])
@login_required
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Returns a list of orders for a user",
            }
        }
    }
)
def getOrders():
    """
    Returns a list of orders for a user
    ---
    """
    result = DataService().get_orders(current_user.id)
    return OrderSchema(many=True).dump(result), 200


@data_api.route("/portfolio", methods=["GET"])
@login_required
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Returns the holdings of the user",
                "schema": PortfolioSchema,
            }
        }
    }
)
def getPortfolio():
    """
    Returns the holdings of the user
    ---
    """
    result = DataService().get_portfolio(current_user.id)
    return jsonify(PortfolioSchema().dump(result)), 200


# ====================
# Coin Gecko API
# ====================
@data_api.route("/coin-list", methods=["GET"])
@login_required
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Returns a list of coins",
            }
        }
    }
)
def getCoinList():
    """
    Returns a list of coins
    ---
    """
    return DataService().get_coin_list(), 200


@data_api.route("/coin-markets", methods=["GET"])
@login_required
@swag_from(
    {
        "responses": {
            HTTPStatus.OK.value: {
                "description": "Returns a list of coins and its associated market data",
            }
        }
    }
)
def getCoinMarkets():
    """
    Returns a list of coins and its associated market data
    ---
    """
    currency = request.args.get("currency", "usd")
    page = request.args.get("page", 1)
    per_page = request.args.get("per_page", 100)
    ids = request.args.get("ids", "")
    return DataService().get_coin_markets(currency, page, per_page, ids), 200
