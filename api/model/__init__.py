from .role import RoleModel
from .userroles import UserRoleModel
from .user import UserModel
from .usersettings import UserSettingsModel
from .serveractivity import ServerActivityModel
from .portfolio import PortfolioModel
from .apikey import ApiKeyModel
from .symbol import SymbolModel
from .currencypair import CurrencyPairModel
from .currencypairconfig import CurrencyPairConfigModel
from .strategyconfig import StrategyConfigModel
from .signal import SignalModel
from .balance import BalanceModel
from .order import OrderModel
from .address import AddressModel

from app import db

RoleModel.users = db.relationship(
    "UserModel",
    secondary="roles_users",
    back_populates="roles"
)

UserModel.roles = db.relationship(
    "RoleModel",
    secondary="roles_users",
    back_populates="users"
)
