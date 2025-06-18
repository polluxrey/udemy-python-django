from django.shortcuts import render

# Create your views here.


def show_book_list(request, slug):
    return render(request, "list/show.html")
