from django.contrib import admin
from .models import Book, Author, Genre

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('title', 'slug')


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Genre)
