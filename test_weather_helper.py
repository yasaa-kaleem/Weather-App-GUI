import pytest
import requests
import weather_helper as wh
from unittest.mock import patch, Mock 
from datetime import datetime

def test_trim_date():
    assert wh.trim_date('2024-01-08 00:00:00') == '2024-01-08'
    assert wh.trim_date('2024-01-08 12:12:12') == '2024-01-08'
    
def test_trim_date_error():
    with pytest.raises(ValueError):
        wh.trim_date('2024-01-08')
        
def test_get_lat_lon_from_zip():
    expected_response = {
        'mocked response'
    }
    with patch('get_location_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = wh.get_lat_lon_from_zip(60108)
        assert response == expected_response
        
def test_get_lat_lon_from_zip_http_error():
    with patch('get_location_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 403
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError

        response = wh.get_lat_lon_from_zip(00000)
        assert "HTTP error occurred" in response
        assert "An error occurred" not in response
        
def test_get_lat_lon_from_zip_exception():
    with patch('get_location_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 403
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.InvalidURL

        response = wh.get_lat_lon_from_zip(00000)
        assert "HTTP error occurred" not in response
        assert "An error occurred" in response
        
def test_get_response_using_lat_lon_fah():
    test_dict = {'lat' : 12345, 'lon' : 67890}
    expected_response = {
        'mocked response'
    }
    with patch('one_day_weather_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = wh.get_one_day_response(test_dict, True)
        assert response == expected_response
        
def test_get_response_using_lat_lon_cel():
    test_dict = {'lat' : 12345, 'lon' : 67890}
    expected_response = {
        'mocked response'
    }
    with patch('one_day_weather_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = wh.get_one_day_response(test_dict, False)
        assert response == expected_response
        
def test_get_multi_day_response_fah():
    test_dict = {'lat' : 12345, 'lon' : 67890}
    expected_response = {
        'mocked response'
    }
    with patch('multi_day_weather_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = wh.get_multi_day_response(test_dict, True)
        assert response == expected_response
        
def test_get_multi_day_response_cel():
    test_dict = {'lat' : 12345, 'lon' : 67890}
    expected_response = {
        'mocked response'
    }
    with patch('multi_day_weather_api.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_response

        response = wh.get_multi_day_response(test_dict, False)
        assert response == expected_response