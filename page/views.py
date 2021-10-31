from django.shortcuts import render
from django.views.generic import ListView
from .models import Project, Knowledge, EEC, Service
from users.models import User

# Create your views here.
class AllPageView(ListView):
    queryset = Project.objects.all().order_by('-modified')
    template_name = 'index.html'
    context_object_name = 'project'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['knowledge'] = Knowledge.objects.all().order_by('modified')
        context['eec'] = EEC.objects.all().order_by('-modified')
        context['service'] = Service.objects.all().order_by('-modified')
        context['procfile'] = User.objects.get(pk=1)
        return context

