from cryptolib.model import CurrencyPairConfigModel as BaseModel
from app import db


class CurrencyPairConfigModel(BaseModel, db.Model):
    pass
