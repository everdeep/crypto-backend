from sqlalchemy import Column, Integer, String, ForeignKey, Enum

from api.enums import ExchangeType
from app import db


class ApiKeyModel(db.Model):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(
        String(32), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    exchange = Column(Enum(ExchangeType), nullable=False)
    api_key = Column(String(255), nullable=False)
    api_secret = Column(String(255), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self) -> str:
        return f"""
            ApiKeyModel(
                id={self.id},
                user_id={self.user_id},
                exchange={self.exchange},
                api_key={self.api_key},
                api_secret={self.api_secret}
            )
        """
