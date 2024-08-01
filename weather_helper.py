from datetime import datetime
from get_location_api import get_location_response
from one_day_weather_api import get_one_day_weather_response
from multi_day_weather_api import get_multi_day_weather_response

# Converts string datetime to datetime object
def convert_str_to_date(str_date):
    try:
        date_time_obj = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        raise ValueError("Date from payload is not in correct format.")
    return date_time_obj

# Trims time out of date
def trim_date(date_in_payload):
    date_time_obj = convert_str_to_date(date_in_payload)
    date_str = date_time_obj.strftime('%Y-%m-%d')
    return date_str

# Gets longitude and latitude from zipcode
def get_lat_lon_from_zip(zip):
    location_dict = get_location_response(zip)
    return location_dict

# Gets one day weather response using latitude, longitude, and temperature unit
def get_one_day_response(location_dict, in_fahrenheit):
    lat = location_dict['lat']
    lon = location_dict['lon']
    if in_fahrenheit:
        lat_lon_response = get_one_day_weather_response(lat, lon, "imperial")
    else:
        lat_lon_response = get_one_day_weather_response(lat, lon, "metric")

    return lat_lon_response

# Gets multi-day weather response
def get_multi_day_response(location_dict, in_fahrenheit):
    lat = location_dict['lat']
    lon = location_dict['lon']
    if in_fahrenheit:
        lat_lon_response = get_multi_day_weather_response(
            lat, lon, "24", "imperial")
    else:
        lat_lon_response = get_multi_day_weather_response(
            lat, lon, "24", "metric")

    return lat_lon_response