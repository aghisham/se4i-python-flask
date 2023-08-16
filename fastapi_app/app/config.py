"""Config File"""

import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=f"{os.getcwd()}/.env")

DEBUG = True if (os.environ.get("DEBUG") in ["1", "True"]) else False
MODE = os.environ.get("MODE") or "development"
APP_VERSION = "0.0.1"
APP_NAME = "FastApi exemple"
APP_DESCRIPTION = "FastApi exemple"
API_PREFIX = "/api"
SQLALCHEMY_DATABASE_URL = (
    os.environ.get("SQLALCHEMY_DATABASE_URL") or "mysql://root:root@localhost/se4idata"
)
