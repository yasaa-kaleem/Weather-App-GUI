# Gets icon location of corresponding weather condtion
def get_icon_per_weather_condition(weather_condition):
    str_condition = str(weather_condition).lower()
    result = ''
    if 'rain' == str_condition or 'drizzle' == str_condition:
        result = 'images/rain.png'
    elif 'thunderstorm' == str_condition:
        result = 'images/thunderstorms.png'
    elif 'clouds' == str_condition:
        result = 'images/cloudy.png'
    elif 'clear' == str_condition:
        result = 'images/clear-day.png'
    else:
        result = 'images/not-available.png'
    return result