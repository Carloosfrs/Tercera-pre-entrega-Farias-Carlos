from django.urls import path
from AppCoder import views


urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cliente', views.Clientes, name="Cliente"),
    path('sobremi', views.Sobremi, name="Sobremi"),
    #path('pedidoFormulario', views.pedidoFormulario, name="PedidoFormulario"),
    #path('vendedorFormulario', views.vendedorFormulario, name="VendedorFormulario"),
    path('buscar/', views.buscar, name="Buscar"),
    #path('post', views.Registroblog, name="Crearpost"),
    path('buscarblog/', views.buscarblog, name="BuscarBlog"),
    path('explorar/', views.blogListView.as_view(), name="Explorar"),
    path('explorar/detalle/<int:pk>/', views.blogDetailView.as_view(), name='Detail'),
    path('explorar/nuevo', views.blogCreateView.as_view(), name='New'),
    path('explorar/editar/<int:pk>/', views.blogUpdate.as_view(), name='Edit'),
    path('blog/eliminar/<int:pk>/', views.blogDelete.as_view(), name='Delete'),
  
    
]