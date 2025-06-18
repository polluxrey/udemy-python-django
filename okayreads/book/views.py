from django.shortcuts import render

# Create your views here.


def show_book(request, slug):
    return render(request, "book/show.html")
