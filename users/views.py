from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_request(request):
    
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
        
        msg_login = "Usuario o contraseña incorrectos"   

    form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})

# Vista de registro
def register(request):

        msg_register = ""
        if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/inicio.html" ,  {"mensaje":"Usuario Creado :)"})

            msg_register = "Error en los datos ingresados"
        else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

        return render(request,"users/registro.html" ,  {"form":form, "msg_register":msg_register})



# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

        
            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:
        datos = {
            'email' : usuario.email,
            'first_name' : usuario.first_name,
            'last_name' : usuario.last_name
            
            
        }
        miFormulario = UserEditForm(initial=datos)

    return render(request, "users/editarPerfil.html", {"mi_form": miFormulario, "usuario": usuario})

from users.forms import AvatarFormulario
from users.models import Avatar
from django.contrib.auth.models import User


@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
        mi_form = AvatarFormulario(request.POST, request.FILES)
        
        if mi_form.is_valid():
            user = User.objects.get(username=request.user)
            
            try:
                avatar = Avatar.objects.get(user=user)
            except Avatar.DoesNotExist:
                avatar = Avatar(user=user, imagen=mi_form.cleaned_data["imagen"])
            else:    
                avatar.imagen = mi_form.cleaned_data['imagen']
            
            avatar.save()
            
            return render(request, "AppCoder/inicio.html")
    else:
        mi_form = AvatarFormulario()
    
    context_data = {"mi_form": mi_form}
    return render(request, "users/agregar_avatar.html", context_data)        
        
    





