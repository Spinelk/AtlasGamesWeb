from django.contrib import admin
from tienda.models import *

# admin.site.register(Usuario)

admin.site.register(Videojuego)
admin.site.register(Genero)
admin.site.register(Estudio)
admin.site.register(PEGI)
admin.site.register(ESBR)


admin.site.register(Noticia)


admin.site.register(Compra)