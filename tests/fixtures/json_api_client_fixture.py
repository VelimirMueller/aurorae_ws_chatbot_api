import pytest
from flask import Flask

from src.api import json_api_bp


@pytest.fixture
def client():
    app = Flask(__name__)
    app.register_blueprint(json_api_bp)
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
