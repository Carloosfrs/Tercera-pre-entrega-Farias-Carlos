from django import forms

class PedidoFormulario(forms.Form):
    
    #Especificar los campos
    pedido = forms.CharField()
    Codigo = forms.IntegerField()
    