from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import BookList, BookListEntry

# Create your views here.


def show_book_list(request, slug):
    if slug == slug.lower():
        redirect('show_book_list', slug=slug.lower(), permanent=True)

    try:
        book_list = BookList.objects.get(slug=slug)
        entries = BookListEntry.objects.filter(
            booklist=book_list).select_related('book')
        context = {
            "book_list": book_list,
            "entries": entries
        }
        return render(request, "list/show.html", context=context)
    except BookList.DoesNotExist:
        return HttpResponseNotFound("Book not found!")
