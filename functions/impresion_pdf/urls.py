from django.urls import path
from .views import generar_boleta_pdf

urlpatterns = [
    path('generar_boleta/', generar_boleta_pdf, name='generar_boleta'),
]
