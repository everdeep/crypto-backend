from cryptolib.model import BalanceModel as BaseModel
from app import db


class BalanceModel(BaseModel, db.Model):
    pass
