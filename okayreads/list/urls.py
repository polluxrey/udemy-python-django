from django.urls import path
from . import views

urlpatterns = [
    path('show/<str:slug>', views.show_book_list, name='show_book_list')
]
