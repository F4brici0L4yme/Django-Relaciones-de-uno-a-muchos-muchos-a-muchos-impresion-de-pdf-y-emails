"""
URL configuration for functions project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emails.urls')),
]

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('lenguaje/', include('relacion_uno_muchos.urls')),  # Ejemplo uno
    path('relacion_muchos_muchos/', include('relacion_muchos_muchos.urls')),  # Ejemplo dos
    path('boleta/', include('impresion_pdf.urls')),  # PDF boleta
    path('emails/', include('emails.urls')),  # Emails
    # Más apps...
]

