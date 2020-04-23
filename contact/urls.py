from django.urls import path

from . import views

urlpatterns = [
    path("contact", views.ContactForm, name="contact"),
    path("contact/Contribution", views.Contribution, name="contribution"),
]
