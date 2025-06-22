from django.db import models
from django.core.validators import MinValueValidator
from book.models import Book
from martor.models import MartorField
from autoslug import AutoSlugField

# Create your models here.


class BookList(models.Model):
    name = models.CharField(max_length=255)
    description = MartorField(blank=True)
    books = models.ManyToManyField(
        Book, through='BookListEntry', related_name='booklists')
    slug = AutoSlugField(populate_from='name',
                         unique=True, always_update=False)


class BookListEntry(models.Model):
    booklist = models.ForeignKey(BookList, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    voters = models.PositiveIntegerField(default=0)

    class Meta:
        # Ensures each book appears only once per booklist
        unique_together = ('booklist', 'book')
