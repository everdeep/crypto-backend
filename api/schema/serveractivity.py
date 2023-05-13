from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from api.model import ServerActivityModel

# IMPORTANT: This is needed to make the marshmallow_sqlalchemy work
# import after the models are defined and before the marshmallow schemas
from sqlalchemy.orm import configure_mappers

configure_mappers()


class ServerActivitySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ServerActivityModel
        include_fk = True
        load_instance = True
