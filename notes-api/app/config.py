import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///notes.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    PAGE_SIZE_DEFAULT = int(os.getenv("PAGE_SIZE_DEFAULT", "10"))
    PAGE_SIZE_MAX = int(os.getenv("PAGE_SIZE_MAX", "100"))
    TESTING = False
