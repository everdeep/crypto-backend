from sqlalchemy import Column, String

from app import db


class SymbolModel(db.Model):
    __tablename__ = "symbols"

    symbol = Column(String(10), primary_key=True, nullable=False)

    currency_pairs = db.relationship(
        "CurrencyPairModel", backref="symbols", cascade="all, delete"
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self) -> str:
        return f"""
            SymbolModel(
                symbol={self.symbol},
                currency_pairs={self.currency_pairs}
            )
        """
