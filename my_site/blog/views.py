import json
import os
from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect

INDEX_POSTS_LIMIT = 3

# Load JSON file for posts
file_path = os.path.join(settings.BASE_DIR, "blog", "data", "posts.json")

with open(file_path, "r", encoding="utf-8") as f:
    posts = json.load(f)

# Load user profile
file_path = os.path.join(settings.BASE_DIR, "static", "data", "user_profile.json")

with open(file_path, "r", encoding="utf-8") as f:
    user = json.load(f)

# Create your views here.

def index(request):
    context = {
        "user": user,
        "recent_posts": posts[-INDEX_POSTS_LIMIT:]
    }

    return render(request, "index.html", context=context)

def view_post(request, slug):
    post = None

    normalized_slug = slug.lower()

    for p in posts:
        if normalized_slug == p["slug"]:
            post = p
            break

    if post is None:
        return HttpResponseNotFound("Article not found!")
    
    if (slug != normalized_slug) and post:
        return redirect(request.path.lower(), permanent=True)

    context = {
        "user": user,
        "post": post,
    }

    return render(request, "post.html", context=context)