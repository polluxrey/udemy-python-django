from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
