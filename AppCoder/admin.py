from django.contrib import admin
from .models import *
from users.models import Avatar
# Register your models here.

admin.site.register(Pedido)

admin.site.register(Cliente)

admin.site.register(Vendedor)

admin.site.register(Carrito)

admin.site.register(Blog)

admin.site.register(Avatar)