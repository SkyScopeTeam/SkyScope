# weather_app/utils.py
import requests
from decouple import config


def get_weather(zip_code):
    api_key = config("TOMORROW_IO_KEY")
    base_url = 'https://api.tomorrow.io/v4/weather/forecast?location=42.3478,-71.0466&apikey=kEONyXCCifCwp205RhhJ3XJX3FGFFepB'
    location_url = f'http://api.zippopotam.us/us/{zip_code}'

    location_response = requests.get(location_url)
    if location_response.status_code != 200:
        return None  # Invalid zip code

    location_data = location_response.json()
    latitude = location_data['places'][0]['latitude']
    longitude = location_data['places'][0]['longitude']

    params = {
        'apikey': api_key,
        'location': f'{latitude},{longitude}',
        'fields': ['temperature', 'weatherCode'],
        'units': 'imperial',  # Use 'metric' for Celsius
        'timesteps': 'current',
    }
    response = requests.get(base_url, params=params)
    return response.json()
