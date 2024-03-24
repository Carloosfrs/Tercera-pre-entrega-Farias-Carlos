from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pedido(models.Model):

    nombre = models.CharField(max_length=40)
    numPedido = models.IntegerField()


class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Vendedor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    nombre_tienda = models.CharField(max_length=30)

class Carrito(models.Model):
    nombre = models.CharField(max_length=30)
    fechadepedido = models.DateField()  
    entregado = models.BooleanField()
    
from django.conf import settings
class Blog(models.Model):
    tema = models.CharField(max_length=15)
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=500)
    fecha = models.DateField(null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='blog_fotos') 
    
    def __str__(self):
        return f"{settings.MEDIA_URL}{self.imagen}"
    
       
    
