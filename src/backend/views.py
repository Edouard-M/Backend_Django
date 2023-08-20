from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html", context={"title": "Backend"})


def test_view(request):
    return HttpResponse("<h1>Test View</h1>")
