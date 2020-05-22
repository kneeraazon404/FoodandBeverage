from django.urls import path

from . import views

urlpatterns = [
    path("payments/", views.HomePageView.as_view(), name="payments"),
    path("charge/", views.charge, name="charge"),
]
