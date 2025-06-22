import json
from datetime import datetime
from book.models import Book, Author, Genre


with open('temp/genres.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    Genre.objects.create(name=item['name'])
