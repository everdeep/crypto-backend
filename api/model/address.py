from cryptolib.model import AddressModel as BaseModel
from app import db


class AddressModel(BaseModel, db.Model):
    pass
