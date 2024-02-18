from django.db import models

# Create your models here.

class Pedido(models.Model):

    nombre=models.CharField(max_length=40)
    pedido = models.IntegerField()


class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Vendedor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    nombre_tienda= models.CharField(max_length=30)

class Carrito(models.Model):
    nombre= models.CharField(max_length=30)
    fechadepedido = models.DateField()  
    entregado = models.BooleanField()
