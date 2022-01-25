from django.contrib import admin
from .models import Projeto, Conhecimento, EEC, Servico

# Register your models here.
admin.site.register(Projeto)
admin.site.register(Conhecimento)
admin.site.register(EEC)
admin.site.register(Servico)
