from django.contrib import admin
from .models import *
# Register your models here.
# Puedes acceder al admin con el usuario admin y contraseña admin
admin.site.register(Deportistas)
admin.site.register(Deportes)
admin.site.register(Entrenadores)
admin.site.register(Participaciones)
admin.site.register(Comentarios)
admin.site.register(Estudiante)
admin.site.register(DeportesDeportistas)