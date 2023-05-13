from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey
from api.enums import Signal

from app import db


class SignalModel(db.Model):
    __tablename__ = "signals"

    id = Column(Integer, primary_key=True)
    currency_pair_config_id = Column(
        Integer,
        ForeignKey("currency_pair_configs.id", ondelete="CASCADE"),
        nullable=False,
    )
    signal = Column(Enum(Signal), nullable=False)
    last_trade_time = Column(DateTime, nullable=False)
    updated_at = Column(
        DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now()
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self) -> str:
        return f"""
            SignalModel(
                id={self.id},
                currency_pair_config_id={self.currency_pair_config_id},
                signal={self.signal},
                last_trade_time={self.last_trade_time},
                updated_at={self.updated_at}
            )
        """
