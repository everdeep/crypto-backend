from marshmallow_enum import EnumField
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from api.enums import RoleType
from api.model import RoleModel

# IMPORTANT: This is needed to make the marshmallow_sqlalchemy work
# import after the models are defined and before the marshmallow schemas
from sqlalchemy.orm import configure_mappers

configure_mappers()


class RoleSchema(SQLAlchemyAutoSchema):
    name = EnumField(RoleType, by_value=True)

    class Meta:
        model = RoleModel
        load_instance = True
