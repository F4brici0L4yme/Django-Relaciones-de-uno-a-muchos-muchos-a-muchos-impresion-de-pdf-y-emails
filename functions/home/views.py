from django.shortcuts import render

# Create your views here.
def index(request):
    ejemplos = [
        {'nombre': 'Relación Uno a Muchos', 'url': 'lenguaje/lenguaje/1/'},
        {'nombre': 'Relación Muchos a Muchos', 'url': 'relacion_muchos_muchos/pelicula/1/'},
        {'nombre': 'Generar PDF (boleta)', 'url': 'boleta/generar_boleta/'},
        {'nombre': 'Enviar Emails', 'url': '/emails/enviar/'},
    ]
    return render(request, 'index.html', {'ejemplos': ejemplos})
