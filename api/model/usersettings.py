from cryptolib.model import UserSettingsModel as BaseModel
from app import db


class UserSettingsModel(BaseModel, db.Model):
    pass
