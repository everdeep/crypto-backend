from cryptolib.model import CurrencyPairModel as BaseModel
from app import db


class CurrencyPairModel(BaseModel, db.Model):
    pass
