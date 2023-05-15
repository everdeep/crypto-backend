from cryptolib.model import ApiKeyModel as BaseModel
from app import db


class ApiKeyModel(BaseModel, db.Model):
    pass
