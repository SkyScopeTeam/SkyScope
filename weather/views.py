from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from tomorrow_io.api import get_forecast


def home_view(request: HttpRequest) -> HttpResponse:
    forecast = get_forecast()
    return render(request, "weather/index.html", {"forecast": forecast})
