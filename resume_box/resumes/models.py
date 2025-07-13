from django.db import models
from django.utils import timezone

# Create your models here.


class ResumeModel(models.Model):
    custom_id = models.CharField(max_length=20, unique=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()

    cover_letter = models.FileField(upload_to='cover_letters/')
    resume = models.FileField(upload_to='resumes/')

    submitted_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.custom_id:
            today = timezone.now().date()
            date_str = today.strftime('%Y%m%d')
            count_today = ResumeModel.objects.filter(
                submitted_at__date=today).count() + 1
            self.custom_id = f"{date_str}-{count_today:03d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.custom_id} - {self.last_name}, {self.first_name}"
