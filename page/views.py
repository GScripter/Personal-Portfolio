from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Project, Knowledge, EEC, Service
from users.models import User
from django.core.mail import send_mail
from django.conf import settings

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


    def post(self, request):
        organizar = (f"nome: {request.POST['name']}\ne-mail: {request.POST['e-mail']}\nmessage: {request.POST['message']}")
        send_mail(
            subject=request.POST['subject'],
            message=organizar,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )
        return render(request, 'success.html')

