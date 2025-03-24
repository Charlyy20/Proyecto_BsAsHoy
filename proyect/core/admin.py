from django.contrib import admin
from .models import Noticia, Categoria

#Gestión de Noticias desde el panel administrador

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'fecha_publicacion')  # Campos a mostrar en la lista
    list_filter = ('categoria', 'fecha_publicacion')  # Filtros laterales
    search_fields = ('titulo', 'contenido')  # Campos de búsqueda
    
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Categoria)