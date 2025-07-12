import json
from datetime import datetime
from blog.models import CustomUser, User, Tag, Post


with open('temp/posts.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    post = Post.objects.get(title=item['title'])

    for tag in item['tags']:
        tag, _ = Tag.objects.get_or_create(name=tag)
        post.tags.add(tag)

    post.save()