from django import forms
from AppCoder.models import Blog
from datetime import date


class PedidoFormulario(forms.Form):
    
    nombre = forms.CharField()
    pedido = forms.IntegerField()
    
class VendedorFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    nombre_tienda = forms.CharField(max_length=30)
    
class Buscar(forms.Form):
    pedido = forms.CharField()


class Clientesform(forms.Form):
    
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()  
    
    
class Blogform(forms.Form):
    tema = forms.CharField(max_length=15)
    titulo = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=500)
    fecha = forms.DateField(initial=date.today, widget=forms.HiddenInput)
    imagen = forms.ImageField()  
    
  
     
    
    
class BuscarBlog(forms.Form):
    tema = forms.CharField()

    

