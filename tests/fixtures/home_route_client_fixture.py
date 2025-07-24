import pytest
from flask import Flask

from src.routes import home_bp


@pytest.fixture
def home_client():
    app = Flask(__name__)
    app.register_blueprint(home_bp)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
