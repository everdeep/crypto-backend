from marshmallow.fields import List
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from api.model import SymbolModel
from utils.marshmallow import Nested

# IMPORTANT: This is needed to make the marshmallow_sqlalchemy work
# import after the models are defined and before the marshmallow schemas
from sqlalchemy.orm import configure_mappers

configure_mappers()


class SymbolSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SymbolModel

    currency_pairs = List(Nested("CurrencyPairSchema"))
