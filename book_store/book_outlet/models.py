from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=2, validators=[
                                 MinValueValidator(1.00), MaxValueValidator(5.00)])
    # Avoid using null on string-based fields such as CharField and TextField.
    # The Django convention is to use an empty string, not NULL, as the “no data” state for string-based fields.
    # If a string-based field has null=True, that means it has two possible values for “no data”: NULL, and the empty string.
    author = models.CharField(blank=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.rating})"
