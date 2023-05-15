from cryptolib.model import SignalModel as BaseModel
from app import db


class SignalModel(BaseModel, db.Model):
    pass
