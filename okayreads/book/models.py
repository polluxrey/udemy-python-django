from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from martor.models import MartorField
from autoslug import AutoSlugField

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = MartorField(blank=True)
    slug = AutoSlugField(populate_from='name',
                         unique=True, always_update=False, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField(
        Author, related_name="books")
    description = MartorField(blank=True)
    genres = models.ManyToManyField(
        Genre, related_name="books")
    published_date = models.DateField(null=True, blank=True)
    ave_rating = models.DecimalField(max_digits=3, decimal_places=2,
                                     default=0.00, validators=[
                                         MinValueValidator(1.00), MaxValueValidator(5.00)])
    raters = models.PositiveIntegerField(default=0)
    slug = AutoSlugField(populate_from='title',
                         unique=True, always_update=False)

    def __str__(self):
        return f"{self.title}"
