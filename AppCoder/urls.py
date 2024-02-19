from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.Pedido, name="Pedido"),
    path('profesores', views.Cliente, name="Clientes"),
    path('estudiantes', views.Vendedor, name="Vendedor"),
    path('entregables', views.Carrito, name="Carrito"),
]