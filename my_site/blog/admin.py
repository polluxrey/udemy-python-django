from django.contrib import admin

from .models import Post, CustomUser, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at",)
    list_filter = ("author",)
    ordering = ("title", "-created_at",)


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(CustomUser)
admin.site.register(Tag)