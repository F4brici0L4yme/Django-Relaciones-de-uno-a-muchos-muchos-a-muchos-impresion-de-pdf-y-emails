from django.shortcuts import render, get_object_or_404
from .models import Pelicula

def personajes_por_pelicula(request, pelicula_id):
    pelicula = get_object_or_404(Pelicula, id=pelicula_id)
    personajes = pelicula.personajes.all()
    return render(request, 'personajes_por_pelicula.html', {
        'pelicula': pelicula,
        'personajes': personajes
    })
