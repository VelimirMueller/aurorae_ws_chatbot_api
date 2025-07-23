# tests/test_api_route.py
from tests.fixtures.home_route_client_fixture import home_client
from unittest.mock import patch

def test_home_status_code(home_client):
    with patch("src.routes.routes.render_template") as mock_render:
        # Simulate the returned HTML string
        mock_render.return_value = "<h1>Mocked Home Page</h1>"

        response = home_client.get('/')

        assert response.status_code == 200
        assert b"<h1>Mocked Home Page</h1>" in response.data
        mock_render.assert_called_once_with("index.html")