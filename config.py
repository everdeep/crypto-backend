import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    

    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # Flask-User settings
    TRACK_USAGE_USE_FREEGEOIP = True
    TRACK_USAGE_FREEGEOIP_ENDPOINT = "https://extreme-ip-lookup.com/json/{ip}?key=Qn97RtiI2gwjStzJJjuG"

    # Logging
    LOG_BASE_PATH = os.getenv("LOG_BASE_PATH")


class DevelopmentConfig(Config):
    DEBUG = True

    # Mail settings
    MAIL_SERVER = os.getenv("MAIL_SERVER_DEV")
    MAIL_PORT = os.getenv("MAIL_PORT_DEV")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME_DEV")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD_DEV")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI_DEV")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class ProductionConfig(Config):
    DEBUG = False

    # Mail settings
    MAIL_SERVER = os.getenv("MAIL_SERVER_PROD")
    MAIL_PORT = os.getenv("MAIL_PORT_PROD")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME_PROD")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD_PROD")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI_PROD")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


if os.environ.get("ENV") == "production":
    app_config = ProductionConfig()
else:
    app_config = DevelopmentConfig()
