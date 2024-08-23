import requests


def get_location_info(zip_code):
    location_url = f'http://api.zippopotam.us/us/{zip_code}'
    location_response = requests.get(location_url)

    return location_response.json()["places"][0]
