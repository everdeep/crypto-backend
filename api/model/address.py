from sqlalchemy import Column, String, Integer, ForeignKey, DateTime

from app import db


class AddressModel(db.Model):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(
        String(32), ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    address_line_1 = Column(String(255), nullable=True)
    address_line_2 = Column(String(255), nullable=True)
    city = Column(String(255), nullable=True)
    state = Column(String(255), nullable=True)
    country = Column(String(255), nullable=True)
    postal_code = Column(String(255), nullable=True)
    updated_at = Column(
        DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now()
    )

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self) -> str:
        return f"""
            AddressModel(
                id={self.id},
                user_id={self.user_id},
                address_line_1={self.address_line_1},
                address_line_2={self.address_line_2},
                city={self.city},
                state={self.state},
                country={self.country},
                postal_code={self.postal_code}
            )
        """
