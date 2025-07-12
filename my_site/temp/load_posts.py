import json
from datetime import datetime
from blog.models import CustomUser, User, Post


with open('temp/posts.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    author = User.objects.get(id=item['author'])
    created_at = datetime.strptime(item['created_at'], "%Y-%m-%d")

    post = Post(title=item['title'],
                content=item['content'],
                author=author,
                created_at=created_at.date())

    post.save()