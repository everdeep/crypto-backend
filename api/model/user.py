from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin

from cryptolib.model import UserModel as BaseModel
from cryptolib.utils.validators import Validator

from app import bcrypt, db


class UserModel(UserMixin, BaseModel, db.Model):
    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        Validator().validate_password(plaintext)
        self._password = bcrypt.generate_password_hash(plaintext).decode("utf-8")
