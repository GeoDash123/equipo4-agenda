import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INSTANCE_DIR = BASE_DIR/"instance"

def _sqlite_uri(filename: str)->str:
    return f"sqlite:///{INSTANCE_DIR/filename}"

class BaseConfig:
    JSON_SORT_KEYS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", _sqlite_uri("dev.sqlite3")
    )