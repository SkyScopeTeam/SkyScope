import requests
from decouple import config

latitude = "38.6270"
longitude = "-90.1994"
TOMORROW_IO_KEY = config("TOMORROW_IO_KEY")
API_URL = "https://api.tomorrow.io/v4"


def get_forecast() -> dict:
    r = requests.get(
        f"{API_URL}/weather/forecast?" +
        f"location={latitude},{longitude}&apikey={TOMORROW_IO_KEY}" +
        "&timesteps=1h&units=imperial"
    )
    return r.json()["timelines"]["hourly"][0]["values"]
