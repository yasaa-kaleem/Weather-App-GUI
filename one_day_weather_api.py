import requests, os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def get_one_day_weather_response(lat, lon, units):
    API_URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units={units}"
    try:
        response = requests.get(API_URL)
        # raise an HTTP error if the response code is not 200
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"

    except Exception as err:
        return f"An error occurred: {err}"