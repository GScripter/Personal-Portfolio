from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Portfolio(TimeStampedModel):
    image = models.FileField(upload_to="portfolio")
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=200)
    link = models.URLField()
    tags = models.CharField(max_length=100)

    def __str__(self):
        return self.title


