def get_icon_per_weather_condition(weather_condition):
    print(weather_condition)
    if "light rain" in weather_condition.lower():
        return 'images/rain.svg'
    elif 'thunderstorm' in weather_condition.lower():
        return 'images/thunderstorms.svg'
    elif 'thunderstorm with' in weather_condition.lower():
        return 'images/thunderstorms-rain.svg'
    elif 'overcast' in weather_condition.lower():
        return 'images/overcast.svg'
    elif 'few clouds' or 'scattered clouds' or 'broken clouds' in weather_condition.lower():
        return 'images/cloudy.svg'
    elif 'clear' in weather_condition.lower():
        return 'images/clear-day.svg'