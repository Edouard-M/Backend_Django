from django.shortcuts import render


def notes(request):
    return render(request, "notes/index.html", context={"title": "Notes App"})
