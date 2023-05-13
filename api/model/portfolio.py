from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey

from app import db


class PortfolioModel(db.Model):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(
        String(32), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    total_earnings = Column(Float, nullable=False, default=0)
    updated_at = Column(
        DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now()
    )

    balances = db.relationship("BalanceModel", backref="portfolio")

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self) -> str:
        return f"""
            PortfolioModel(
                id={self.id},
                user_id={self.user_id},
                total_earnings={self.total_earnings},
                updated_at={self.updated_at},
            )
        """
