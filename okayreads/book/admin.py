from django.contrib import admin
from .models import Book, Author, Genre

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('title', 'slug')

    list_display = ('title', 'ave_rating',)
    list_filter = ('authors')
    list_per_page = 10


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Genre)
