from django.shortcuts import render

from tomorrow_io.api import get_forecast
from zippopotam.api import get_location_info


def home_view(request):
    if request.method != 'POST':
        return render(request, 'weather/weather.html')

    zip_code = request.POST.get('zip_code')
    location_info = get_location_info(zip_code)
    latitude = location_info["latitude"]
    longitude = location_info["longitude"]
    location_info["city"] = location_info["place name"]

    weather = get_forecast(latitude=latitude, longitude=longitude)
    return render(
        request,
        'weather/index.html',
        {
            'weather': weather,
            "location": location_info
        }
    )
