import pytest

from app import create_app
from app import db as _db


@pytest.fixture()
def app():
    app = create_app(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        }
    )
    with app.app_context():
        _db.create_all()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
