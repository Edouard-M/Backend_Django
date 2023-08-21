from django.contrib import admin
# from django.views.defaults import server_error
from django.urls import include, path
from .views import index, weather


urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('weather/', weather, name="weather"),
    path('notes/', include("notes.urls")),
]
