from cryptolib.model import *
from cryptolib.enums import *
import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

ENGINE = create_engine(
    Config().SQLALCHEMY_DATABASE_URI, echo=False, pool_size=20, max_overflow=0
)

# ========================
# Fixtures
# ========================


@pytest.fixture
def session():
    """Create a new session"""
    Session = sessionmaker(bind=ENGINE)
    session = Session()
    yield session
    session.close()


# ========================
# NOTE: When doing a len() on  dict, there is 1 extra key called _sa_instance_state


# ========================
# Tests
# ========================
def test_address_model(session):
    """Test the address model"""
    data = session.query(AddressModel).first()
    assert "id" in data.__dict__
    assert "address_line_1" in data.__dict__
    assert "address_line_2" in data.__dict__
    assert "city" in data.__dict__
    assert "state" in data.__dict__
    assert "country" in data.__dict__
    assert "postal_code" in data.__dict__
    assert len(data.__dict__.keys()) - 1 == 7


def test_api_key_model(session):
    """Test the api_key model"""
    data = session.query(ApiKeyModel).first()
    assert "id" in data.__dict__
    assert "user_id" in data.__dict__
    assert "api_key" in data.__dict__
    assert "api_secret" in data.__dict__
    assert "exchange" in data.__dict__
    assert type(data.exchange) == ExchangeType
    assert len(data.__dict__.keys()) - 1 == 5


def test_signal_model(session):
    """Test the autotrade model"""
    data = session.query(SignalModel).first()
    assert "id" in data.__dict__
    assert "signal" in data.__dict__
    assert type(data.signal) == signal
    assert "last_trade_time" in data.__dict__
    assert "updated_at" in data.__dict__
    assert len(data.__dict__.keys()) - 1 == 4


def test_balance_model(session):
    """Test the balance model"""
    data = session.query(BalanceModel).first()
    assert "id" in data.__dict__
    assert "portfolio_id" in data.__dict__
    assert "exchange" in data.__dict__
    assert type(data.exchange) == ExchangeType
    assert "asset" in data.__dict__
    assert "free" in data.__dict__
    assert "locked" in data.__dict__
    assert "total" in data.__dict__
    assert "updated_at" in data.__dict__
    assert len(data.__dict__.keys()) - 1 == 8


def test_currency_pair_model(session):
    """Test the currency_pair model"""
    data = session.query(CurrencyPairModel).first()
    assert "currency_pair" in data.__dict__
    assert "symbol" in data.__dict__
    assert "pair" in data.__dict__
    assert len(data.__dict__.keys()) - 1 == 3


def test_currency_pair_config_model(session):
    """Test the currency_pair_config model"""
    data = session.query(CurrencyPairConfigModel).first()
    assert "id" in data.__dict__
    assert "user_id" in data.__dict__
    assert "currency_pair" in data.__dict__
    assert "bot_name" in data.__dict__
    assert "exchange" in data.__dict__
    assert type(data.exchange) == ExchangeType
    assert "interval" in data.__dict__
    assert type(data.interval) == Interval
    assert "tradeable" in data.__dict__
    assert "strategy" in data.__dict__
    assert type(data.strategy) == StrategyType
    assert "limit" in data.__dict__
    assert "signal_id" in data.__dict__
    assert "stop_loss" in data.__dict__
    assert "take_profit" in data.__dict__
    assert "asset_allocation" in data.__dict__
    assert "is_active" in data.__dict__
    assert "is_simulated" in data.__dict__
    assert "updated_at" in data.__dict__
    assert len(data.__dict__.keys()) - 1 == 16


def test_order_model(session):
    """Test the order model"""
    data = session.query(OrderModel).first()
    assert "id" in data.__dict__
    assert "user_id" in data.__dict__
    assert "currency_pair" in data.__dict__
    assert "order_id" in data.__dict__
    assert "bot_id" in data.__dict__
    assert "exchange" in data.__dict__
    assert type(data.exchange) == ExchangeType
    assert "cost" in data.__dict__
    assert "last_price" in data.__dict__
    assert "amount" in data.__dict__
    assert "side" in data.__dict__
    assert type(data.side) == OrderSide
    assert "status" in data.__dict__
    assert type(data.status) == OrderStatus
    assert "type" in data.__dict__
    assert type(data.type) == OrderType
    assert "limit_price" in data.__dict__
    assert "is_autotraded" in data.__dict__
    assert "is_simulated" in data.__dict__
    assert "created_at" in data.__dict__
    assert "updated_at" in data.__dict__
    assert len(data.__dict__.keys()) - 1 == 17


def test_portfolio_model(session):
    """Test the portfolio model"""
    data = session.query(PortfolioModel).first()
    assert "id" in data.__dict__
    assert "user_id" in data.__dict__
    assert "total_cost" in data.__dict__
    assert "updated_at" in data.__dict__
    assert len(data.__dict__.keys()) - 1 == 4


def test_strategy_config_model(session):
    """Test the strategy_config model"""
    data = session.query(StrategyConfigModel).first()
    assert "id" in data.__dict__
    assert "currency_pair_config_id" in data.__dict__
    assert "strategy" in data.__dict__
    assert type(data.strategy) == StrategyType
    assert "key" in data.__dict__
    assert "value" in data.__dict__
    assert len(data.__dict__.keys()) - 1 == 5


def test_symbol_model(session):
    """Test the symbols model"""
    data = session.query(SymbolModel).first()
    assert "symbol" in data.__dict__
    assert len(data.__dict__.keys()) - 1 == 1


def test_user_model(session):
    """Test the user model"""
    data = session.query(UserModel).first()
    assert "id" in data.__dict__
    assert "email" in data.__dict__
    assert "_password" in data.__dict__
    assert "first_name" in data.__dict__
    assert "last_name" in data.__dict__
    assert "username" in data.__dict__
    assert "dob" in data.__dict__
    assert "phone" in data.__dict__
    assert "address_id" in data.__dict__
    assert "portfolio_id" in data.__dict__
    assert "is_admin" in data.__dict__
    assert "is_active" in data.__dict__
    assert "is_verified" in data.__dict__
    assert "created_at" in data.__dict__
    assert "updated_at" in data.__dict__
    assert len(data.__dict__.keys()) - 1 == 15


def test_user_settings_model(session):
    """Test the user_settings model"""
    data = session.query(UserSettingsModel).first()
    assert "id" in data.__dict__
    assert "user_id" in data.__dict__
    assert "key" in data.__dict__
    assert "value" in data.__dict__
    assert len(data.__dict__.keys()) - 1 == 4


def test_role_model(session):
    """Test the role model"""
    data = session.query(RoleModel).first()
    assert "id" in data.__dict__
    assert "name" in data.__dict__
    assert type(data.name) == RoleType
    assert "description" in data.__dict__
    assert len(data.__dict__.keys()) - 1 == 3


def test_server_activity_model(session):
    """Test the server_activity model"""
    data = session.query(ServerActivityModel).first()
    if data is None:
        return
    assert "id" in data.__dict__
    assert "url" in data.__dict__
    assert "ua_browser" in data.__dict__
    assert "ua_language" in data.__dict__
    assert "ua_platform" in data.__dict__
    assert "ua_version" in data.__dict__
    assert "blueprint" in data.__dict__
    assert "view_args" in data.__dict__
    assert "status" in data.__dict__
    assert "remote_addr" in data.__dict__
    assert "xforwardedfor" in data.__dict__
    assert "authorization" in data.__dict__
    assert "ip_info" in data.__dict__
    assert "path" in data.__dict__
    assert "speed" in data.__dict__
    assert "datetime" in data.__dict__
    assert "username" in data.__dict__
    assert "user_id" in data.__dict__
    assert "track_var" in data.__dict__
    assert len(data.__dict__.keys()) - 1 == 19
