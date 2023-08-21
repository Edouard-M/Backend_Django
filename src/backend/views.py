from django.http import HttpResponse
from django.shortcuts import render

from backend.weather.weather_utils import WEATHER_CONTEXT, compare_weather, fetch_weather, post_weather_api


def index(request):
    return render(request, "index.html", context={"title": "Backend"})


def notes(request):
    return render(request, "notes_app.html", context={"title": "Notes App"})


def weather(request):
    if request.method == "POST":
        post_weather_api(request)

    return render(request, "weather.html", WEATHER_CONTEXT)


def test_view(request):
    return HttpResponse("<h1>Test View</h1>")
