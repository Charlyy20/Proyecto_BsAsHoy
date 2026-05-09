from django.contrib import admin
from .models import BannerCliente, BannerClienteGif, FotoNoticia, VideoExterno


@admin.register(BannerCliente)
class BannerClienteAdmin(admin.ModelAdmin):
    list_display = ("titulo", "cliente", "activo", "creado")
    list_filter = ("activo", "creado")
    search_fields = ("titulo", "cliente")

@admin.register(BannerClienteGif)
class BannerClienteGifAdmin(admin.ModelAdmin):
    list_display = ("titulo", "cliente", "activo", "creado")
    list_filter = ("activo", "creado")
    search_fields = ("titulo", "cliente")
@admin.register(FotoNoticia)
class FotoNoticiaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "creado")
    search_fields = ("titulo", "descripcion")


@admin.register(VideoExterno)
class VideoExternoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "plataforma", "activo", "creado")
    list_filter = ("plataforma", "activo", "creado")
    search_fields = ("titulo", "descripcion", "url_video")