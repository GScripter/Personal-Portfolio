from django.shortcuts import render
from django.views.generic import ListView
from .models import Projeto, Conhecimento, EEC, Servico
from users.models import User
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
class PagePTView(ListView):
    queryset = Projeto.objects.all().order_by('-modified')
    template_name = 'page-pt.html'
    context_object_name = 'projeto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfil'] = User.objects.get(username='Gabriel55693')
        context['conhecimento'] = Conhecimento.objects.all().order_by('modified')
        context['eec'] = EEC.objects.all().order_by('-modified')
        context['servico'] = Servico.objects.all().order_by('-modified')
        return context


    def post(self, request):
        organizar = (f"nome: {request.POST['name']}\ne-mail: {request.POST['e-mail']}\nmessage: {request.POST['message']}")
        send_mail(
            subject=request.POST['subject'],
            message=organizar,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )
        return render(request, 'success-pt.html')

