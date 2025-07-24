from unittest.mock import MagicMock, patch

import pytest
from flask import Flask, json

from src.chat import chat_session, single_response


# Import your function, adjust the import path accordingly:
# from src.chat_module import chat_session
@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    return app


def test_chat_session_exit():
    model = MagicMock()
    model.current_chat_session = "Previous chat data"
    socket = MagicMock()

    chat_session("exit", model, socket)

    # Check socket.send calls on exit input
    assert socket.send.call_count == 2
    socket.send.assert_any_call("printing previous chat session, restarting session")
    socket.send.assert_any_call("Previous chat data")


def test_chat_session_non_exit():
    model = MagicMock()
    model.generate.return_value = "AI generated answer"
    socket = MagicMock()

    chat_session("Hello", model, socket)

    # model.generate called with user_input
    model.generate.assert_called_once_with("Hello")
    # socket.send called once with AI answer
    socket.send.assert_called_once_with("AI generated answer")

    def test_single_response_success(app):
        user_input = "Hello"

        # Mock api_model in the module where single_response is defined
        with patch("src.chat.api_model") as m:
            m.chat_session.return_value.__enter__.return_value = None
            m.chat_session.return_value.__exit__.return_value = None
            m.generate.return_value = "AI generated response"

            with app.app_context():
                response = single_response(user_input)
                data = json.loads(response.get_data())

                assert response.status_code == 200
                assert "data" in data
                assert data["data"]["request"] == user_input
                assert (
                    data["data"]["server_response"]
                    == "Received request, answering with json"
                )
                assert data["data"]["ai_response"] == "AI generated response"
