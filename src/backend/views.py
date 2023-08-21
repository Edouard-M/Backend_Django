from django.http import HttpResponse
from django.shortcuts import render
import requests


def index(request):
    return render(request, "index.html", context={"title": "Backend"})


def test_view(request):
    return HttpResponse("<h1>Test View</h1>")


WEATHER_CONTEXT = {
    "title": "Weather App",
    "weather_data1": None,
    "weather_data2": None,
}


def weather(request):
    API_KEY = "6729f3a667ecb47bfa3f03a220d899d1"
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    weather_data1 = None
    weather_data2 = None

    if request.method == "POST":
        city1 = request.POST.get("city1", None)
        city2 = request.POST.get("city2", None)

        if city1:
            weather_data1 = fetch_weather(city=city1, api_key=API_KEY, current_weather_url=current_weather_url)
            WEATHER_CONTEXT["weather_data1"] = weather_data1

        if city2:
            weather_data2 = fetch_weather(city=city2, api_key=API_KEY, current_weather_url=current_weather_url)
            WEATHER_CONTEXT["weather_data2"] = weather_data2

    return render(request, "weather.html", WEATHER_CONTEXT)


def fetch_weather(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()

    weather_data = {
        "city": city,
        "temperature": round(response['main']['temp'] - 273.15, 1),
        "description": response['weather'][0]['description'],
        "icon": response['weather'][0]['icon']
    }

    return weather_data
