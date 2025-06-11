import json
import os
from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

import re
import random
import string
from datetime import datetime, timezone
import copy

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
    if request.method == "POST":
        slug = f"{slugify(request.POST['title'].strip())}-{len(temp_posts)+1}"

        short_url = generate_random_string()
        dt_now = datetime.now(timezone.utc)
        created_at = dt_now.isoformat()

        new_post = {
            "id": len(temp_posts) + 1,
            "title": request.POST['title'].strip(),
            "slug": slug,
            "short_url": short_url,
            "content": request.POST['content'].strip(),
            "image_url": request.POST['image_url'].strip(),
            "created_at": created_at,
            "published": True
        }

        posts.append(new_post)

        with open(posts_file_path, 'w') as f:
            json.dump(posts, f, indent=4)

        new_post["created_at"] = dt_now.strftime("%B %d, %Y")

        temp_posts.append(new_post)

        messages.success(request, "Article posted successfully!")

        return redirect('MDlmY')

    context = {
        "user": user,
        "recent_posts": temp_posts[-INDEX_POSTS_LIMIT:]
    }

    return render(request, "index.html", context=context)


def view_post(request, slug):
    post = None

    normalized_slug = slug.lower()

    for p in temp_posts:
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


def view_all_posts(request):
    if len(temp_posts) == 0:
        return HttpResponseNotFound("No articles found!")

    page = request.GET.get('page', 1)

    paginator = Paginator(temp_posts[::-1], 3)

    try:
        posts_by_page = paginator.page(page)
    except PageNotAnInteger:
        posts_by_page = paginator.page(1)
    except EmptyPage:
        posts_by_page = paginator.page(paginator.num_pages)

    context = {
        "user": user,
        "posts": posts_by_page,
    }

    return render(request, "posts.html", context=context)


def about_me(request):
    context = {
        "user": user
    }

    return render(request, "about-me.html", context=context)
