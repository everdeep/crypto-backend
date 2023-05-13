from sqlalchemy import Column, Integer

from app import db


class UserRoleModel(db.Model):
    __tablename__ = "roles_users"

    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    role_id = Column(
        Integer, db.ForeignKey("roles.id", ondelete="CASCADE"), nullable=False
    )
