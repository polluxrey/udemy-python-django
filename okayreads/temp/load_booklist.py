import json
from book.models import Book
from list.models import BookList, BookListEntry


with open('temp/booklist.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    booklist = BookList(
        name=item['name'],
        description=item['description']
    )

    booklist.save()

    for book in item['books']:
        print(book['title'])
        book_temp = Book.objects.get(title=book['title'])
        BookListEntry.objects.create(
            booklist=booklist,
            book=book_temp,
            score=book['score'],
            voters=book['voters']
        )
