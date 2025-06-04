from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenge_by_number, name="month-challenge-num"),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]
