from django.urls import path
from . import views

urlpatterns = [
    path('show/<str:slug>', views.show_book, name='show_book')
]
