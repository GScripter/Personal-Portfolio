from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    photo = models.FileField(upload_to="photo", blank=True)
    name = models.CharField(max_length=250, blank=False)
    about = models.TextField(blank=False)
    city = models.CharField(max_length=30, blank=False)
    cv = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    modified = models.DateTimeField(auto_now=True)

