from django.shortcuts import render
from django.views.generic import ListView
from .models import Portfolio

# Create your views here.
class AllPageView(ListView):
    queryset = Portfolio.objects.all().order_by('-modified')
    template_name = 'index.html'
    context_object_name = 'project'

