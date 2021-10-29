from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    photo = models.ImageField(upload_to="photo", blank=True)
    name = models.CharField(max_length=250)
    about = models.TextField(blank=True)
    city = models.CharField(max_length=30)
    cv = models.URLField(blank=True)

