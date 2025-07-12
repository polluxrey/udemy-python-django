from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from martor.models import MartorField
from django_extensions.db.fields import AutoSlugField, CreationDateTimeField, ModificationDateTimeField

# Create your models here.


class SocialPlatform(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BlogSettings(models.Model):
    blog_name = models.CharField(max_length=20)
    bio = MartorField(max_length=100, default="")
    about_me = MartorField()
    profile_image = models.ImageField(
        upload_to='blog/profile_images/', blank=True, null=True)
    social_links = models.ManyToManyField(
        SocialPlatform, through='SocialLink')

    def clean(self):
        # if there’s already one in the DB, block creation of any others
        if BlogSettings.objects.exists() and not self.pk:
            raise ValidationError("Only one BlogSettings may exist.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.blog_name


class SocialLink(models.Model):
    blog = models.ForeignKey(BlogSettings, on_delete=models.CASCADE)
    platform = models.ForeignKey(SocialPlatform, on_delete=models.CASCADE)
    url = models.URLField()

    class Meta:
        unique_together = ('blog', 'platform')

    def __str__(self):
        return f"{self.platform.name}: {self.url}"


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = MartorField()
    birth_date = models.DateField()

    def __str__(self):
        return self.user.get_full_name()


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = MartorField()
    image = models.ImageField(
        upload_to='blog/cover_images/', blank=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="posts")
    created_at = CreationDateTimeField(blank=False)
    modified_at = ModificationDateTimeField(blank=False)
    tags = models.ManyToManyField(Tag)
    slug = AutoSlugField(populate_from="title", blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

    class Meta:
        permissions = (
            ("read", "Can view posts"),
            ("delete_posts", "Can delete own posts"),
            ("edit_posts", "Can edit own posts"),
            ("delete_published_posts", "Can delete own published posts"),
            ("edit_published_posts", "Can edit own published posts"),
            ("publish_posts", "Can publish posts"),
            ("delete_others_posts", "Can delete posts created by other users"),
            ("edit_others_posts", "Can edit posts created by other users"),
        )
