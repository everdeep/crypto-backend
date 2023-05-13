import json
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from api.model import ServerActivityModel
from api.enums import UserActions

# IMPORTANT: This is needed to make the marshmallow_sqlalchemy work
# import after the models are defined and before the marshmallow schemas
from sqlalchemy.orm import configure_mappers

configure_mappers()


## Not used
class IpInfoSchema(Schema):
    asn = fields.Str()
    asnName = fields.Str()
    asnOrg = fields.Str()
    businessName = fields.Str()
    businessWebsite = fields.Str()
    city = fields.Str()
    continent = fields.Str()
    country = fields.Str()
    countryCode = fields.Str()
    ipName = fields.Str()
    ipType = fields.Str()
    isp = fields.Str()
    lat = fields.Str()
    lon = fields.Str()
    org = fields.Str()
    query = fields.Str()
    region = fields.Str()
    status = fields.Str()
    timezone = fields.Str()
    utcOffset = fields.Str()

    def load(self, data, *args, **kwargs):
        return super().load(json.loads(data), *args, **kwargs)

    def dump(self, data, *args, **kwargs):
        return super().dump(data, *args, **kwargs)


class Endpoint(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        try:
            return UserActions(value).name
        except ValueError:
            return value

    def _deserialize(self, value, attr, data, **kwargs):
        try:
            return UserActions[value].value
        except KeyError:
            return value


class UserActivitySchema(SQLAlchemyAutoSchema):
    endpoint = Endpoint()

    # ip_info = IpInfo()
    class Meta:
        fields = (
            "id",
            "user_id",
            "ip_info",
            "endpoint",
            "url",
            "status",
            "remote_addr",
            "datetime",
        )

        model = ServerActivityModel
        include_fk = True
        load_instance = True
