import json
from datetime import datetime
from book.models import Book, Author, Genre


with open('temp/authors.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    Author.objects.create(name=item['name'],
                          bio=item['bio'])
