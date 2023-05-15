from cryptolib.model import OrderModel as BaseModel
from app import db


class OrderModel(BaseModel, db.Model):
    pass
