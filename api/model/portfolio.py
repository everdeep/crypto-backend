from cryptolib.model import PortfolioModel as BaseModel
from app import db


class PortfolioModel(BaseModel, db.Model):
    pass
