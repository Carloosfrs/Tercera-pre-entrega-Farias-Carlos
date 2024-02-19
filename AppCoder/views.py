from django.shortcuts import render, HttpResponse


# Create your views here.
def inicio(request):

      return HttpResponse("vista inicio")


def Pedido(request):

      return HttpResponse("vista Pedido")


def Cliente(request):

      return HttpResponse("vista Cliente")

def Vendedor(request):

    return HttpResponse("vista Vendedor")

def Carrito (request):

    return HttpResponse("Vista Carrito")