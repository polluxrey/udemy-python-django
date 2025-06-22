import json
from datetime import datetime
from book.models import Book, Author, Genre


with open('temp/books.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    book = Book(title=item['title'],
                description=item['description'],
                published_date=datetime.strptime(
                    item['published_date'], "%Y-%m-%d"),
                ave_rating=item['ave_rating'],
                raters=item['raters'])

    book.save()

    for author in item['authors']:
        try:
            author_temp = Author.objects.get(name=author)
            book.authors.add(author_temp)
        except Author.DoesNotExist:
            print("Object not found!")
            continue
        except Author.MultipleObjectsReturned:
            print("Multiple objects found!")
            continue

    for genre in item['genres']:
        try:
            genre_temp = Genre.objects.get(name=genre)
            book.genres.add(genre_temp)
        except Genre.DoesNotExist:
            print("Object not found!")
            continue
        except Genre.MultipleObjectsReturned:
            print("Multiple objects found!")
            continue

    book.save()
