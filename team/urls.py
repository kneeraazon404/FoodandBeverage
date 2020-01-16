from django.urls import path
from . import views

urlpatterns = [
    path("team/", views.team, name="team"),
]
