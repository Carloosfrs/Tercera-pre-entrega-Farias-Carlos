from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.forms import PedidoFormulario, VendedorFormulario, Buscar,Blogform, BuscarBlog
from .models import Pedido, Vendedor, Blog
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from users.models import Avatar
from django.utils import timezone
from .forms import Blogform




# Create your views here.
def inicio(request):
      try:
            avatares = Avatar.objects.get(user=request.user.id)
            imagen = avatares.imagen.url
      except:
            imagen = ""     
      
      
      return render(request, "AppCoder/Inicio.html", {"url": imagen})



def pedido(request):
      return render(request, "AppCoder/Pedido.html")


def Clientes(request):

      return render(request, "AppCoder/Cliente.html")

def Vendedores(request):

      return render(request, "AppCoder/Vendedor.html")

def Sobremi (request):

      return render(request, "AppCoder/Sobremi.html")

@login_required #para que pida loguearse en funciones
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
            
def buscarblog(request):
      
      if request.method == "POST":
            miFormulario = BuscarBlog(request.POST)
            if miFormulario.is_valid():
                  info = miFormulario.cleaned_data
                  print(info["tema"])
                  tema = Blog.objects.filter(tema__icontains=info["tema"])
                  print(tema)
                  return render(request, "AppCoder/buscarblog.html", {"temas":tema})  
      else:
            miFormulario = BuscarBlog()  
      
            return render(request, "AppCoder/buscarblog.html", {"formulario": miFormulario}) 
        
            
      

@login_required #para que pida loguearse en funciones
def Registroblog(request):
 
      if request.method == "POST":
 
            miFormulario = Blogform(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  blog = Blog (tema=informacion["tema"], titulo=informacion["titulo"], descripcion=informacion["descripcion"])
                  blog.save()
                  return render(request, "AppCoder/inicio.html")
      else:
            miFormulario = Blogform()
 
      return render(request, "AppCoder/blog.html", {"form": miFormulario})


class blogListView(ListView):
      model = Blog
      template_name = "AppCoder/bloglist.html"
      
class blogDetailView(DetailView):
      model = Blog
      template_name = "AppCoder/blogdetalle.html"
      
class blogCreateView(LoginRequiredMixin, CreateView):
      model = Blog
      template_name = "AppCoder/blogformview.html"
      success_url = "/"
      fields = ["tema", "titulo", "descripcion", "imagen"]
      
      def form_valid(self, form):
        # Establece la fecha actual en el campo de fecha antes de guardar el formulario
        form.instance.fecha = timezone.now().date()
        form.instance.autor = self.request.user
        form.instance.imagen = self.request.FILES.get('imagen')
        return super().form_valid(form)
      


   

class blogUpdate(LoginRequiredMixin, UpdateView):
      model = Blog   
      template_name = "AppCoder/blogformview.html"
      success_url = "/"
      fields = "__all__"
      
      


class blogDelete(LoginRequiredMixin, DeleteView):
      model = Blog
      template_name = "AppCoder/blogeliminar.html"
      success_url = "/"
      
  
