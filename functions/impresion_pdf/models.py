from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Boleta(models.Model):
    productos = models.ManyToManyField(Producto)
    fecha = models.DateTimeField(auto_now_add=True)
