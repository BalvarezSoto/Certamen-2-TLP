from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to="media", null=True)
    
    def __str__(self):
        return f'{self.nombre}->{self.precio}'

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    total = models.IntegerField()
    estado = models.CharField(max_length=10, choices=[('pendiente', 'Pendiente'), ('completado', 'Completado')], default='pendiente')

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.username}"



