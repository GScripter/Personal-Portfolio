from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Projeto(TimeStampedModel):
    imagem = models.FileField(upload_to="project", blank=True)
    nome = models.CharField(max_length=50, blank=False)
    texto = models.CharField(max_length=200, blank=False)
    link = models.URLField(blank=False)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome


class Conhecimento(TimeStampedModel):
    logo = models.FileField(upload_to="logo", blank=False)
    nome = models.CharField(max_length=20, blank=False)
    alt = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.nome


class EEC(TimeStampedModel):
    CATEGORIA = (
        ('educação','Educação'),
        ('experiência','Experiência'),
        ('curso','Curso'),
    )
    data = models.CharField(max_length=25, blank=False)
    nome = models.CharField(max_length=60, blank=False)
    texto = models.CharField(max_length=150, blank=False)
    categoria = models.CharField(max_length=12, blank=False, choices=CATEGORIA, default='educação')

    def __str__(self):
        return self.nome


class Servico(TimeStampedModel):
    logo = models.FileField(upload_to="logo", blank=False)
    nome = models.CharField(max_length=20, blank=False)
    texto = models.CharField(max_length=150, blank=False)
    alt = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.nome

