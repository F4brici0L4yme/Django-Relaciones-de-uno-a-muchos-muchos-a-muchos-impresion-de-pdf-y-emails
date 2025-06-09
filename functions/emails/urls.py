from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_email, name='enviar_email'),
    path('enviado/', views.email_enviado, name='email_enviado'),
]
