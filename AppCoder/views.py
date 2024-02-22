from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import PedidoFormulario
from .models import Pedido

# Create your views here.
def inicio(request):

      return render(request, "AppCoder/Inicio.html")


def pedido(request):

      return render(request, "AppCoder/Pedido.html")


def Cliente(request):

      return render(request, "AppCoder/Cliente.html")

def Vendedor(request):

      return render(request, "AppCoder/Vendedor.html")

def Carrito (request):

      return render(request, "AppCoder/Carrito.html")

def pedidoFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = PedidoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  pedido = Pedido (nombre=informacion["nombre"], numPedido=informacion["pedido"])
                  pedido.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = PedidoFormulario()
 
      return render(request, "AppCoder/pedidoFormulario.html", {"miFormulario": miFormulario})