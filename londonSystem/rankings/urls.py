from django.urls import path
from . import views

urlpatterns = [
    # path("", views.reload_button, name="btn-reload"),
    path("", views.index, name="index"),
    path("games.html", views.games, name="games"),
    path("btn-reload", views.reload_button, name="btn-reload")
]