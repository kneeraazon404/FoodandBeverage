from django.urls import path

from . import views

urlpatterns = [
    path("payments/", views.HomePageView.as_view(), name="payments"),
    path("charge/", views.payments, name="charge"),
    path("charge/", views.stripe, name="charge"),
]
