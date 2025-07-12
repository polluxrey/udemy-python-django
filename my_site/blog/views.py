import json
import os
from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

import re
import random
import string
from datetime import datetime, timezone
import copy

from blog.models import Post, BlogSettings

INDEX_POSTS_LIMIT = 3

# Load JSON file for posts
posts_file_path = os.path.join(settings.BASE_DIR, "blog", "data", "posts.json")

with open(posts_file_path, "r", encoding="utf-8") as f:
    posts = json.load(f)

temp_posts = copy.deepcopy(posts)

for post in temp_posts:
    iso_date = post["created_at"]
    dt = datetime.fromisoformat(iso_date)
    post["created_at"] = dt.strftime("%B %d, %Y")

# Load user profile
user_profile_file_path = os.path.join(settings.BASE_DIR, "static",
                                      "data", "user_profile.json")

with open(user_profile_file_path, "r", encoding="utf-8") as f:
    user = json.load(f)


def generate_random_string(length=5):
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    return ''.join(random.choices(characters, k=length))


def slugify(text):
    # Convert to lowercase
    text = text.lower()

    # Replace spaces with hyphens
    text = text.replace(' ', '-')

    # Remove non-alphanumeric characters except hyphens
    text = re.sub(r'[^a-z0-9-]', '', text)

    # Remove multiple hyphens
    text = re.sub(r'--+', '-', text)

    return text


# Create your views here.

def index(request):
    context = {
        "user": request.user,
        "blog_settings": BlogSettings.objects.first(),
        "recent_posts": Post.objects.all().order_by('-created_at')[:INDEX_POSTS_LIMIT]
    }

    return render(request, "index.html", context=context)


def view_post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        context = {
            "user": request.user,
            "blog_settings": BlogSettings.objects.first(),
            "post": post,
        }

        return render(request, "post.html", context=context)
    except Post.DoesNotExist:
        return HttpResponseNotFound("Article not found!")


def view_all_posts(request):
    if Post.objects.count() == 0:
        return HttpResponseNotFound("No articles found!")

    page = request.GET.get('page', 1)

    paginator = Paginator(Post.objects.all().order_by('-created_at'), 3)

    try:
        posts_by_page = paginator.page(page)
    except PageNotAnInteger:
        posts_by_page = paginator.page(1)
    except EmptyPage:
        posts_by_page = paginator.page(paginator.num_pages)

    context = {
        "user": request.user,
        "blog_settings": BlogSettings.objects.first(),
        "posts": posts_by_page,
    }

    return render(request, "posts.html", context=context)


def about_me(request):
    context = {
        "blog_settings": BlogSettings.objects.first()
    }

    return render(request, "about-me.html", context=context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        print(username)
        print("hello")

        if user is not None:
            login(request, user)
            return redirect('MDlmY')  # Replace with your homepage view name
        else:
            messages.error(request, 'Invalid username or password')

    return redirect('MDlmY')


def logout_view(request):
    logout(request)
    return redirect('MDlmY')  # Redirect to login page after logout


def write_new_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        content = request.POST.get('content')

        post = Post(title=title, content=content, image=image)
        post.save()

        messages.success(request, "Successfully posted!")

    return redirect('MDlmY')
