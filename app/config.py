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

#read data from config.yaml one time and share it between the files
import json

with open('app/config.yaml', 'r') as file:
    config_data = json.load(file)

mongodb_host = config_data["mongodb"]["host"]
port = config_data["mongodb"]["port"]
database_name = config_data["mongodb"]["database_name"]
collection_name = config_data["mongodb"]["collection_name"]
user_name = config_data["jwt_credentials"]["user_name"]
password = config_data["jwt_credentials"]["password"]
user_id = config_data["jwt_credentials"]["user_id"]
api = config_data["api"]["host"]