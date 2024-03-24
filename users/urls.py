from django.urls import path 
from users import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login', views.login_request, name="login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppCoder/inicio.html'), name='Logout'),   
    path('editarPerfil', views.editarPerfil, name="editarperfil"), 
    path('agregar_avatar', views.agregar_avatar, name="AgregarAvatar")
]