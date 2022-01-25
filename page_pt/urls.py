from django.urls import path
from . import views

urlpatterns = [
    path('', views.PagePTView.as_view(), name='pt'),
]


