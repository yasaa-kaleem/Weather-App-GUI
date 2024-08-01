import requests
from unittest.mock import patch
from one_day_weather_api import get_one_day_weather_response

def test_get_weather_response_sucess():
    expected_response = {
        "mocked response",
    }
    with patch('weather_api.requests.get') as mock_request:
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = expected_response

        response = get_one_day_weather_response("","")
        assert response == expected_response

def test_get_weather_response_http_error():
    with patch('weather_api.requests.get') as mock_request:
        mock_request.return_value.status_code = 403
        mock_request.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError

        response = get_one_day_weather_response("","")
        assert "HTTP error occurred" in response