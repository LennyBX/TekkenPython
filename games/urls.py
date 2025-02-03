from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("jeux1/", include("games.jeux1.urls")),
    path("admin/", admin.site.urls),
]