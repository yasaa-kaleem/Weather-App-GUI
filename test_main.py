# import pytest
# import get_location_api
# from main import start_program
# from unittest.mock import patch
# from unittest.mock import MagicMock
# import weather_api

# @patch('get_location_api.get_location_response', 'weather_api.get_weather_response')
# def test_start_program(self, get_content_mock, monkeypatch):
#     mock_input = "60108"
#     monkeypatch.setattr('builtins.input', lambda _: mock_input)

#     get_content_mock.return_value = 'mocked stuff'

#     my_mod = get_location_api
#     self.assertEqual(my_mod.get_location_response(), 'mocked stuff')

#     my_mod2 = weather_api
#     self.assertEqual(my_mod2.get_weather_response(), 'mocked stuff')



#     result = start_program()
#     print(result)