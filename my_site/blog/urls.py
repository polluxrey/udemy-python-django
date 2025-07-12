from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="MDlmY"),
    path("posts/", views.view_all_posts, name="qAtTF"),
    path("post/create/", views.write_new_post, name="VoeLr"),
    path("post/<str:slug>/", views.view_post, name="rcOrH"),
    path("about-me/", views.about_me, name="jXl6k"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
