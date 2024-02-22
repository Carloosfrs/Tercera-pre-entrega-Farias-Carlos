from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import PedidoFormulario


# Create your views here.
def inicio(request):

      return render(request, "AppCoder/index.html")


def pedido(request):

      return HttpResponse("vista Pedido")


def Cliente(request):

      return HttpResponse("vista Cliente")

def Vendedor(request):

      return HttpResponse("vista Vendedor")

def Carrito (request):

      return HttpResponse("Vista Carrito")

def pedidoFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = PedidoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  Pedido = pedido(nombre=informacion["nombre"], numPedido=informacion["pedido"])
                  Pedido.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = PedidoFormulario()
 
      return render(request, "AppCoder/pedidoFormulario.html", {"miFormulario": miFormulario})