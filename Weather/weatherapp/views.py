# weather_app/views.py
from django.shortcuts import render
from .utils import get_weather

#def weather_view(request):
#    weather_data = None
#    if request.method == 'POST':
#        zip_code = request.POST.get('zip_code')
#        weather_data = get_weather(zip_code)
#        print(weather_data)  # Print the API response to inspect its structure
#   return render(request, 'weatherapp/weather.html', {'weather_data': weather_data})


def weather_view(request):
    weather_data = None
    context = {}
    if request.method == 'POST':
        zip_code = request.POST.get('zip_code')
        weather_data = get_weather(zip_code)
        
        if weather_data and 'data' in weather_data:
            timelines = weather_data['data']['timelines']
            if timelines and len(timelines) > 0:
                intervals = timelines[0]['intervals']
                if intervals and len(intervals) > 0:
                    values = intervals[0]['values']
                    temperature = values.get('temperature')
                    weather_code = values.get('weatherCode')
                    context['temperature'] = temperature
                    context['weather_code'] = weather_code
                    context['location'] = zip_code

    print(context)  # Print the context to debug
    return render(request, 'weatherapp/weather.html', context)