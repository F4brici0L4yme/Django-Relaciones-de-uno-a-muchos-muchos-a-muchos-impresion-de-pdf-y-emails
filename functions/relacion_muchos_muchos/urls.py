from django.urls import path
from . import views

urlpatterns = [
    path('pelicula/<int:pelicula_id>/', views.personajes_por_pelicula, name='personajes_por_pelicula'),
]
