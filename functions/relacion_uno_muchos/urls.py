from django.urls import path
from . import views

urlpatterns = [
    path('lenguaje/<int:lenguaje_id>/', views.frameworks_por_lenguaje, name='frameworks_por_lenguaje'),
]
