from django.contrib import admin
from .models import Project, Knowledge, EEC, Service

# Register your models here.
admin.site.register(Project)
admin.site.register(Knowledge)
admin.site.register(EEC)
admin.site.register(Service)

