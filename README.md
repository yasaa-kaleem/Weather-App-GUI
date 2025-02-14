# Weather App GUI
A simple and minimalist Weather Application that shows current weather or has option to show multi-day (3-day) weather in Fahrenheit or Celsius.

## Overview
This app allows the user to view weather of any zipcode within the US. App fetches data from an open source external API, OpenWeather. It has the ability to make multiple calls to the api to get weather data. First call is made to get Longitude and Latitude of the zipcode. Other calls are made to either get data for current weather or multi-day in Fahrenheit or Celsius unit.

## Features
- Minimalist view
- Ability to show Current or Multi-Day weather
- Shows Weather Condition Icons
- Shows Weather description
- Ability to show weather in Celsius

## Downloading 
1. Here's the link to download/ clone this repository:
    https://gitlab.galvanize.com/yasaa.kaleem.ee1h/weather-app-gui

    HTTPS clone:
    git clone https://gitlab.galvanize.com/yasaa.kaleem.ee1h/weather-app-gui.git

## How it works
1. Open terminal.
2. Go to the root directory of the project.
3. Do python main.py.
4. Once app opens, type in the zipcode of the city.
5. Options - You have the option to select Multi-Day to view 3-day weather and to view Temperature in Celsius.
6. When either one of the options are select, Get Weather button needs to be click again to update values.

## Key Notes
1. This app works with an API Key. Please visit https://openweathermap.org/api to get your personal API Key.
    - Once the key is accquired, create a ".env" file in the root directory.
    - Within the .env file, add API_KEY=Your Key and save the file

2. This app requires additional packages to be installed before app can we used.
    - In the terminal make sure you are on the root directory.
    - Create a virtual environment by doing:
        1. python -m venv ./virt_env
        2. ./virt_env/Scripts/activate
    - Once virtual environment has been created, install all required packages by:
        1. pip install -r requirements.txt

## Screenshots
- ![Main Screen](/screenshots/Main%20screen.png "Main Screen")
- ![One day weather in Fahrenheit](/screenshots/One%20Day%20weather%20screen.png "One day weather in Fahrenheit")
- ![One day weather in Celsius](/screenshots/One%20Day%20weather%20C%20screen.png "One day weather in Celsius")
- ![Multi-day weather in Fahrenheit](/screenshots/Multi-day%20weather%20screen.png "Multi-day weather in Fahrenheit")
- ![Multi-day weather in Celsius](/screenshots/Multi-day%20weather%20C%20screen.png "Multi-day weather in Celsius")
- ![Error Screen](/screenshots/Error%20screen.png "Error Screen")