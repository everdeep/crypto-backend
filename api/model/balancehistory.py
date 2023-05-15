from cryptolib.model import BalanceHistoryModel as BaseModel
from app import db


class BalanceHistoryModel(BaseModel, db.Model):
    pass
