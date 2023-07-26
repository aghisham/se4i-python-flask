import logging
import uuid
import datetime
import os


logging.basicConfig(
    level=logging.INFO | logging.ERROR,
    filename="log.log",
    format="%(asctime)s %(levelname)s %(message)s",
)


class Configurations:
    """Configurations Class"""

    # ---------- JWT
    SECRET_KEY = uuid.uuid4().hex
    JWT_EXPERATION_DELTA = datetime.timedelta(days=2)
    JWT_AUTH_URL_RULE = "/auth"


class DevelopmentConfig(Configurations):
    """Development Configuration Class"""

    DEBUG = os.environ.get("DEBUG") or True
    MONGO_URI = os.environ.get("MONGO_URI") or "mongodb://localhost:27017/se4idata"


class TestingConfig(Configurations):
    """Testing Configuration Class"""

    DEBUG = os.environ.get("DEBUG") or False
    TESTING = os.environ.get("TESTING") or True
    MONGO_URI = os.environ.get("MONGO_URI") or "mongodb://localhost:27017/se4idata"


class ProductionConfig(Configurations):
    """Production Configuration Class"""

    DEBUG = os.environ.get("DEBUG") or False
    MONGO_URI = os.environ.get("MONGO_URI") or ""


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
