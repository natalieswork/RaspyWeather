import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass


@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int


load_dotenv()
api_key = os.getenv('API_KEY')


def get_lat_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(
        f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data = resp[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon


def get_current_weather(lat, lon, API_key):
    resp = requests.get(
        f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={API_key}&units=imperial').json()
    current_weather = resp.get('current', {})

    if 'weather' in current_weather and len(current_weather['weather']) > 0:
        weather_info = current_weather['weather'][0]
        main = weather_info.get('main')
        description = weather_info.get('description')
        icon = weather_info.get('icon')
    else:
        main = description = icon = "N/A"

    temperature = int(current_weather.get('temp', "N/A"))

    data = WeatherData(main=main, description=description,
                       icon=icon, temperature=temperature)
    return data


def main(city_name, state_name, country_name):
    lat, lon = get_lat_lon(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data


if __name__ == "__main__":
    lat, lon = get_lat_lon('Toronto', 'ON', 'Canada', api_key)
    print(get_current_weather(lat, lon, api_key))
