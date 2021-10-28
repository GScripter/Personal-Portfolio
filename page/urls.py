from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllPageView.as_view(), name='all'),
]

