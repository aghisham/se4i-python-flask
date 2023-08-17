import os
from django.conf import settings
from dotenv import load_dotenv

load_dotenv(dotenv_path=f"{os.getcwd()}/.env")


engines = {
    "sqlite": "django.db.backends.sqlite3",
    "mysql": "django.db.backends.mysql",
}


def config():
    """Database config

    Returns:
        dict
    """
    service_name = os.getenv("DATABASE_SERVICE_NAME", "").upper().replace("-", "_")
    engine = os.getenv("DATABASE_ENGINE")
    if not service_name or not engine:
        engine = engines["sqlite"]
    name = os.getenv("DATABASE_NAME")
    if not name and engine == engines["sqlite"]:
        name = os.path.join(settings.BASE_DIR, "db.sqlite3")
    return {
        "ENGINE": engine,
        "NAME": name,
        "USER": os.getenv("DATABASE_USER"),
        "PASSWORD": os.getenv("DATABASE_PASSWORD"),
        "HOST": os.getenv("HOST"),
        "PORT": os.getenv("PORT"),
    }
