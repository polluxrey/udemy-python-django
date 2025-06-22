from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import Book
# Create your views here.


def show_book(request, slug):
    if slug == slug.lower():
        redirect('show_book', slug=slug.lower(), permanent=True)

    try:
        book = Book.objects.get(slug=slug)
        context = {
            "book": book
        }
        return render(request, "book/show.html", context=context)
    except Book.DoesNotExist:
        return HttpResponseNotFound("Book not found!")
