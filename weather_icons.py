def get_icon_per_weather_condition(weather_condition):
    str_condition = str(weather_condition).lower()
    result = ''
    if "light rain" in str_condition:
        result = 'images/rain.png'
    elif 'thunderstorm' in str_condition:
        result = 'images/thunderstorms.png'
    elif 'thunderstorm with' in str_condition:
        result = 'images/thunderstorms-rain.png'
    elif 'overcast' in str_condition:
        result = 'images/overcast.png'
    elif 'few clouds' in str_condition or 'scattered clouds' in str_condition or 'broken clouds' in str_condition:
        result = 'images/cloudy.png'
    elif 'clear' in str_condition:
        result = 'images/clear-day.png'
    return result