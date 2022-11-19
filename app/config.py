import os


class Config(object):
    CURRENT_VERSION = "0.0.0"


class TestConfig(Config):
    # these variables get ignored somehow...
    ENV = "development"
    DEBUG = True
    DB_NAME = "localtest.db"
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"
    SECRET_KEY = os.environ.get(
            "SECRET_KEY",
            "debugging_key"
            )

class ProductionConfig(Config):
    ENV = "production"
    PORT = 5000
    DB_NAME = ""
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{DB_NAME}"
    SECRET_KEY = os.environ.get(
            "SECRET_KEY",
            )
