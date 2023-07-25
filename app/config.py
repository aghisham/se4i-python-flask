import logging
import uuid
import datetime


logging.basicConfig(
    level=logging.INFO | logging.ERROR,
    filename="log.log",
    format="%(asctime)s %(levelname)s %(message)s",
)


class Configurations:
    """Configurations Class"""

    # JWT
    SECRET_KEY = uuid.uuid4().hex
    JWT_EXPERATION_DELTA = datetime.timedelta(days=2)
    JWT_AUTH_URL_RULE = "/auth"


class DevelopmentConfig(Configurations):
    """Development Configuration Class"""

    DEBUG = True
    MONGO_URI = "mongodb://localhost:27017/se4idata"


class TestingConfig(Configurations):
    """Testing Configuration Class"""

    DEBUG = False
    TESTING = True
    MONGO_URI = "mongodb://localhost:27017/se4idata"


class ProductionConfig(Configurations):
    """Production Configuration Class"""

    DEBUG = False
    MONGO_URI = ""


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
