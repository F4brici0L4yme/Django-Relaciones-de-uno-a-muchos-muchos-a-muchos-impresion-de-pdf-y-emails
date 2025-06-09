from django.contrib import admin

# Register your models here.
from .models import Pelicula, Personaje

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    filter_horizontal = ('personajes',)

@admin.register(Personaje)
class PersonajeAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
