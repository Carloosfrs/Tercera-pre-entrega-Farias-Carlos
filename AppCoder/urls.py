from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cliente', views.Cliente, name="Cliente"),
    path('carrito', views.Carrito, name="Carrito"),
    path('pedidoFormulario', views.pedidoFormulario, name="PedidoFormulario"),
    path('vendedorFormulario', views.vendedorFormulario, name="VendedorFormulario"),
    path('buscar/', views.buscar, name="Buscar")
]