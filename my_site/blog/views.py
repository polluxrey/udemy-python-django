import json
import os
from django.conf import settings
from django.shortcuts import render

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
