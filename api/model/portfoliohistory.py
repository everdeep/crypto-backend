from cryptolib.model import PortfolioHistoryModel as BaseModel
from app import db


class PortfolioHistoryModel(BaseModel, db.Model):
    pass
