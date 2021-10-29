from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Project(TimeStampedModel):
    image = models.FileField(upload_to="project", blank=True)
    name = models.CharField(max_length=50, blank=False)
    text = models.CharField(max_length=200, blank=False)
    link = models.URLField(blank=False)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Knowledge(TimeStampedModel):
    logo = models.FileField(upload_to="logo", blank=False)
    name = models.CharField(max_length=20, blank=False)
    alt = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name


class EEC(TimeStampedModel):
    CATEGORY = (
        ('education','Education'),
        ('experience','Experience'),
        ('course','Course'),
    )
    date = models.CharField(max_length=25, blank=False)
    name = models.CharField(max_length=60, blank=False)
    text = models.CharField(max_length=150, blank=False)
    category = models.CharField(max_length=12, blank=False, choices=CATEGORY, default='education')

    def __str__(self):
        return self.name


class Service(TimeStampedModel):
    logo = models.FileField(upload_to="logo", blank=False)
    name = models.CharField(max_length=20, blank=False)
    text = models.CharField(max_length=150, blank=False)
    alt = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name

