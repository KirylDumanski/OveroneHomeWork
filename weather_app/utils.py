from datetime import datetime

import geocoder
import requests

WEATHER_TOKEN = '2fd6d5c272d1eef15c8baff08893c4fa'


def get_weather(city: str = None) -> [dict, None]:
    url = 'https://api.openweathermap.org/data/2.5/weather'
    if city is None:
        lat, lon = geocoder.ip('me').latlng
        response = requests.get(url, params={'lat': lat,
                                             'lon': lon,
                                             'units': 'metric',
                                             'appid': WEATHER_TOKEN}).json()
    else:
        response = requests.get(url, params={'q': city,
                                             'units': 'metric',
                                             'appid': WEATHER_TOKEN}).json()

    if response['cod'] == '404':
        return None

    city = response['name']
    temperature = round(response['main']['temp'])
    feels_like = round(response['main']['feels_like'])
    icon = response['weather'][0]['icon']
    time = datetime.fromtimestamp(response['dt'])
    description = response['weather'][0]['description'].title()
    wind_speed = response['wind']['speed']
    wind_deg = response['wind']['deg']
    pressure = round(response['main']['pressure'] / 1.333)  # get value in hPa, div by 1.333 to get mm. hg.
    humidity = response['main']['humidity']
    visibility = round(response['visibility'] / 1000, 1)  # get value in m, div by 1000 to get km

    context = {
        'city': city,
        'temperature': {
            'actual': temperature,
            'feels_like': feels_like,
        },
        'icon': icon,
        'time': time,
        'description': description,
        'wind': {
            'speed': wind_speed,
            'deg': wind_deg,
        },
        'pressure': pressure,
        'humidity': humidity,
        'visibility': visibility
    }
    return context
