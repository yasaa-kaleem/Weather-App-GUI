import requests, os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

def get_location_response(zip_code):
    API_URL = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code}&appid={api_key}"
    try:
        response = requests.get(API_URL)
        # raise an HTTP error if the response code is not 200
        response.raise_for_status()
        location_data = response.json()
        return location_data
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"

    except Exception as err:
        return f"An error occurred: {err}"