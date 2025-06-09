from django.db import models

# Create your models here.
class Personaje(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    personajes = models.ManyToManyField(Personaje)

    def __str__(self):
        return self.titulo