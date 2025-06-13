from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="MDlmY"),
    path("posts/", views.view_all_posts, name="qAtTF"),
    # path("post/create/", views.create_post, name="VoeLr"),
    path("post/<str:slug>/", views.view_post, name="rcOrH"),
    path("post/s/<str:short_url>/", views.view_post_short_url, name="taURc"),
    path("about-me/", views.about_me, name="jXl6k")
]