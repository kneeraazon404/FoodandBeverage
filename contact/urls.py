from django.urls import path

from . import views

urlpatterns = [
    path("contact", views.Contact, name="contact"),
    path("contact/Contribution", views.Contribution, name="contribution"),
]
