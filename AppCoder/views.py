from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import PedidoFormulario, VendedorFormulario, Buscar
from .models import Pedido, Vendedor

# Create your views here.
def inicio(request):

      return render(request, "AppCoder/Inicio.html")


def pedido(request):

      return render(request, "AppCoder/Pedido.html")


def Cliente(request):

      return render(request, "AppCoder/Cliente.html")

def Vendedores(request):

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


def vendedorFormulario(request):

      if request.method == 'POST':

            miFormulario = VendedorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  vendedor = Vendedor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'], nombre_tienda=informacion['nombre_tienda']) 

                  vendedor.save()

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= VendedorFormulario() #Formulario vacio para construir el html

      return render(request, "AppCoder/vendedorFormulario.html", {"miFormulario":miFormulario})
 


def buscar(request):
      
      if request.method == "POST":
            miFormulario = Buscar(request.POST)
            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  print(info["pedido"])
                  pedido = Pedido.objects.filter(numPedido__icontains=info["pedido"])
                  print(pedido)
                  return render(request, "AppCoder/buscar.html", {"pedidos":pedido})  
      else:
            miFormulario = Buscar()  
      
            return render(request, "AppCoder/buscar.html", {"formulario": miFormulario})     
            
            
            
