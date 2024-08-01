from weather_icons import get_icon_per_weather_condition

def test_get_icon_per_weather_condition():
    assert get_icon_per_weather_condition('Rain') == 'images/rain.png'
    assert get_icon_per_weather_condition('Drizzle') == 'images/rain.png'
    assert get_icon_per_weather_condition('Thunderstorm') == 'images/thunderstorms.png'
    assert get_icon_per_weather_condition('Clouds') == 'images/cloudy.png'
    assert get_icon_per_weather_condition('Clear') == 'images/clear-day.png'
    assert get_icon_per_weather_condition('Hail') == 'images/not-available.png'