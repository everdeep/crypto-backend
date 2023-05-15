from cryptolib.model import SymbolModel as BaseModel
from app import db


class SymbolModel(BaseModel, db.Model):
    pass
