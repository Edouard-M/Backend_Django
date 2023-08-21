from django.shortcuts import render
from .models import Notes


def notes(request):
    all_notes = Notes.objects.all()

    context = {
        "title": "Notes App",
        "all_notes": all_notes,
    }

    return render(request, "notes/index.html", context=context)


def note(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, "notes/note.html", context={"note": note})


def add_note(request):

    if request.method == "POST":
        title = request.POST.get("title", None)
        body = request.POST.get("body", None)
        if title:
            Notes.objects.create(title=title, body=body)

    return render(request, "notes/add.html", context={})
