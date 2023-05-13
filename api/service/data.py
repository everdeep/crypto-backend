import requests
from api.model import SymbolModel, CurrencyPairConfigModel, OrderModel, BalanceModel, PortfolioModel

from app import db


class DataService:
    def get_symbols(self):
        """Returns all symbols"""
        return SymbolModel.query.order_by(SymbolModel.symbol).all()

    def get_symbol(self, symbol):
        """Returns all currency pairs for a symbol"""
        return SymbolModel.query.filter_by(symbol=symbol).first()

    def get_currency_pair_config(self, user_id, currency_pair):
        """Returns a currency pair config for a user"""
        return CurrencyPairConfigModel.query.filter_by(currency_pair=currency_pair, user_id=user_id).first()

    def get_currency_pair_configs(self, user_id, args):
        """Returns all currency pair configs for a user"""
        is_active = args.get("is_active", None, type=bool)
        if is_active is not None:
            return CurrencyPairConfigModel.query.filter_by(user_id=user_id, is_active=is_active).order_by(
                CurrencyPairConfigModel.currency_pair
            ).all()

        return CurrencyPairConfigModel.query.filter_by(user_id=user_id).all()


    def get_orders(self, user_id):
        """Returns all orders for a user"""
        return OrderModel.query.filter_by(user_id=user_id).order_by(OrderModel.created_at.desc()).all()

    def get_portfolio(self, user_id):
        """Returns a portfolio for a user"""
        return PortfolioModel.query.filter_by(user_id=user_id).first()

    def get_balances(self, portfolio_id):
        """Returns all balances for a user"""
        return BalanceModel.query.filter_by(portfolio_id=portfolio_id).all()

    def get_balance(self, portfolio_id, asset):
        """Returns a balance for a user"""
        return BalanceModel.query.filter_by(portfolio_id=portfolio_id, asset=asset).first()

    # ===================================
    # Updates
    # ===================================

    def update_portfolio(self, user_id, portfolio):
        """Updates a portfolio for a user"""
        portfolio = PortfolioModel.query.filter_by(user_id=user_id).first()
        if portfolio:
            # TODO: Update portfolio

            # db.session.commit()
            return portfolio

        return None

    def update_currency_pair_config(self, currency_pair, user_id, config):
        currency_pair_config = CurrencyPairConfigModel.query.filter_by(
            currency_pair=currency_pair, user_id=user_id
        ).first()
        if currency_pair_config:
            # TODO: Update config

            # db.session.commit()
            return currency_pair_config

        return None

    # ===================================
    # Coin Gecko API
    # https://www.coingecko.com/en/api
    # ===================================
    def get_coin(self, coin_id):
        return requests.get(f"https://api.coingecko.com/api/v3/coins/{coin_id}").json()

    def get_coin_list(self):
        return requests.get("https://api.coingecko.com/api/v3/coins/list").json()

    def get_coin_markets(self, currency, page, per_page, ids):
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": currency,
            "ids": ids,
            "order": "market_cap_desc",
            "per_page": per_page,
            "page": page,
            "sparkline": "false",
        }
        return requests.get(url, params, timeout=10).json()
