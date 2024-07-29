import requests
from unittest.mock import patch
from get_location_api import get_location_response

def test_get_location_response_sucess():
    expected_response = {
        "mocked response",
    }

    with patch('get_location_api.requests.get') as mock_request:
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = expected_response

        response = get_location_response("")
        assert response == expected_response


def test_get_location_response_http_error():
    with patch('get_location_api.requests.get') as mock_request:
        mock_request.return_value.status_code = 403
        mock_request.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError

        response = get_location_response("")
        assert "HTTP error occurred" in response