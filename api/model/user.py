from sqlalchemy import Column, Boolean, String, Date, DateTime, ForeignKey, Integer
from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin

from utils.validators import Validator

from uuid import uuid4

from app import db, bcrypt


def get_uuid():
    return uuid4().hex


class UserModel(UserMixin, db.Model):
    __tablename__ = "users"

    id = Column(
        String(32), primary_key=True, default=get_uuid, unique=True, nullable=False
    )
    email = Column(String(255), nullable=False)
    _password = Column(String(128), nullable=False)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    username = Column(String(128), nullable=True)
    dob = Column(Date, nullable=True)
    phone = Column(String(64), nullable=True)
    is_admin = Column(Boolean, nullable=False, default=0)
    is_active = Column(Boolean, nullable=False, default=1)
    is_verified = Column(Boolean, nullable=False, default=0)
    created_at = Column(DateTime, nullable=False, default=db.func.now())
    updated_at = Column(
        DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now()
    )

    address = db.relationship(
        "AddressModel", backref="users", cascade="all, delete", uselist=False
    )
    portfolio = db.relationship(
        "PortfolioModel", backref="users", cascade="all, delete", uselist=False
    )
    settings = db.relationship(
        "UserSettingsModel", backref="users", cascade="all, delete"
    )
    api_keys = db.relationship("ApiKeyModel", backref="users", cascade="all, delete")
    orders = db.relationship("OrderModel", backref="users", cascade="all, delete")
    currency_pair_configs = db.relationship(
        "CurrencyPairConfigModel", backref="users", cascade="all, delete"
    )
    activity = db.relationship(
        "ServerActivityModel", backref="users", cascade="all, delete"
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext):
        Validator().validate_password(plaintext)
        self._password = bcrypt.generate_password_hash(plaintext).decode("utf-8")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self) -> str:
        return f"""
            UserModel(
                id={self.id},
                email={self.email},
                _password={self._password},
                first_name={self.first_name},
                last_name={self.last_name},
                username={self.username},
                dob={self.dob},
                phone={self.phone},
                is_admin={self.is_admin},
                is_active={self.is_active},
                is_verified={self.is_verified},
                created_at={self.created_at},
                updated_at={self.updated_at},
                settings={self.settings},
                address={self.address},
                portfolio={self.portfolio}
            )
        """
