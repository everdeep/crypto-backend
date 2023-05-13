from sqlalchemy import Column, Integer, String, Enum
from api.enums import RoleType


from app import db


class RoleModel(db.Model):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(Enum(RoleType), unique=True)
    description = Column(String(255))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self) -> str:
        return f"""
            RoleModel(
                id={self.id},
                name={self.name},
                description={self.description},
            )
        """
