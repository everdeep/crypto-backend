from marshmallow.fields import List
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from api.model import UserModel
from utils.marshmallow import Nested

# IMPORTANT: This is needed to make the marshmallow_sqlalchemy work
# import after the models are defined and before the marshmallow schemas
from sqlalchemy.orm import configure_mappers

configure_mappers()


class UserSchema(SQLAlchemyAutoSchema):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "username",
            "dob",
            "phone",
            "address",
            "portfolio",
            "settings",
            "roles",
            "is_verified",
            # "orders",
            # "currency_pair_configs",
        )
        model = UserModel
        load_instance = True

    settings = List(Nested("UserSettingsSchema"))
    address = Nested("AddressSchema")
    portfolio = Nested("PortfolioSchema")
    roles = List(Nested("RoleSchema"))
    # api_keys = List(Nested("ApiKeySchema"))
    # orders = List(Nested("OrderSchema"))
    # currency_pair_configs = List(Nested("CurrencyPairConfigSchema"))
    # activity = List(Nested("UserActivitySchema"))