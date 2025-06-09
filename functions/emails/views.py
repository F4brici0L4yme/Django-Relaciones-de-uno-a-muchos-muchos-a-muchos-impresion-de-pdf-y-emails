from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse

def enviar_email(request):
    if request.method == 'POST':
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')
        email_destino = request.POST.get('email_destino')

        send_mail(
            asunto,
            mensaje,
            settings.DEFAULT_FROM_EMAIL,
            [email_destino],
            fail_silently=False,
        )
        return HttpResponseRedirect(reverse('email_enviado'))

    return render(request, 'enviar_email.html')

def email_enviado(request):
    return render(request, 'email_enviado.html')
