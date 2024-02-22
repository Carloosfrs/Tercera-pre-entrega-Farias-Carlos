from django import forms

class PedidoFormulario(forms.Form):
    
    nombre = forms.CharField()
    pedido = forms.IntegerField()
    