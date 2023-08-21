from django.urls import path
from .views import notes, note, add_note

urlpatterns = [
    path('', notes, name="notes"),
    path('<int:pk>', note, name="note"),
    path('add/', add_note, name="add_note"),
]
