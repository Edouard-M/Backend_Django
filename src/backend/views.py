from django.http import HttpResponse
from django.shortcuts import render

from backend.weather.weather_utils import WEATHER_CONTEXT, post_weather_api


def index(request):
    return render(request, "backend/index.html", context={"title": "Backend"})


def weather(request):
    if request.method == "POST":
        post_weather_api(request)

    return render(request, "backend/weather.html", WEATHER_CONTEXT)


def test_view(request):
    return HttpResponse("<h1>Test View</h1>")
