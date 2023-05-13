from sqlalchemy import Column, String, ForeignKey

from app import db


class CurrencyPairModel(db.Model):
    __tablename__ = "currency_pairs"

    currency_pair = Column(String(20), nullable=False, primary_key=True)
    symbol = Column(
        String(10), ForeignKey("symbols.symbol", ondelete="CASCADE"), nullable=False
    )
    pair = Column(String(10), nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self) -> str:
        return f"""
            CurrencyPairModel(
                currency_pair={self.currency_pair}
                symbol={self.symbol},
                pair={self.pair}
            )
        """
