from django import forms

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
    