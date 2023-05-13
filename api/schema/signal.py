from marshmallow_enum import EnumField
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from api.enums import Signal
from api.model import SignalModel

# IMPORTANT: This is needed to make the marshmallow_sqlalchemy work
# import after the models are defined and before the marshmallow schemas
from sqlalchemy.orm import configure_mappers

configure_mappers()


class SignalSchema(SQLAlchemyAutoSchema):
    signal = EnumField(Signal, dump_by=EnumField.NAME, load_by=EnumField.NAME)

    class Meta:
        model = SignalModel
        include_fk = True
        load_instance = True
