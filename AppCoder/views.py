from django.shortcuts import render, HttpResponse


# Create your views here.
def inicio(request):

      return render(request, "AppCoder/index.html")


def Pedido(request):

      return HttpResponse("vista Pedido")


def Cliente(request):

      return HttpResponse("vista Cliente")

def Vendedor(request):

      return HttpResponse("vista Vendedor")

def Carrito (request):

      return HttpResponse("Vista Carrito")

def pedidoFormulario(request):
      if request.method == 'POST':
      
            pedido =  Pedido(request.post['curso'],(request.post['camada']))
 
            pedido.save()
 
            return render(request, "AppCoder/inicio.html")
 
      return render(request,"AppCoder/pedidoFormulario.html")