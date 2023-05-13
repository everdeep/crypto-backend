from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey,
    Integer,
    JSON,
    Float,
    Boolean,
)

from app import db


class ServerActivityModel(db.Model):
    __tablename__ = "server_activity"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(255))
    endpoint = Column(String(128))
    ua_browser = Column(String(16))
    ua_language = Column(String(16))
    ua_platform = Column(String(16))
    ua_version = Column(String(16))
    blueprint = Column(String(16))
    view_args = Column(String(64))
    status = Column(Integer)
    remote_addr = Column(String(24))
    xforwardedfor = Column(String(24))
    authorization = Column(Boolean)
    ip_info = Column(JSON)
    path = Column(String(32))
    speed = Column(Float)
    datetime = Column(DateTime)
    username = Column(String(128))
    user_id = Column(String(32), ForeignKey("users.id"))
    track_var = Column(String(128))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return f"""
        ServerActivityModel(
            id={self.id},
            url={self.url},
            endpoint={self.endpoint},
            ua_browser={self.ua_browser},
            ua_language={self.ua_language},
            ua_platform={self.ua_platform},
            ua_version={self.ua_version},
            blueprint={self.blueprint},
            view_args={self.view_args},
            status={self.status},
            remote_addr={self.remote_addr},
            xforwardedfor={self.xforwardedfor},
            authorization={self.authorization},
            ip_info={self.ip_info},
            path={self.path},
            speed={self.speed},
            datetime={self.datetime},
            username={self.username},
            user_id={self.user_id},
            track_var={self.track_var}
        )
        """
