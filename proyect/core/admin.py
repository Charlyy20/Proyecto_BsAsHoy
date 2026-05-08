from django.contrib import admin
from .models import BannerCliente, BannerClienteGif, FotoNoticia, VideoMp4


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


@admin.register(VideoMp4)
class VideoMp4Admin(admin.ModelAdmin):
    list_display = ("titulo", "creado")
    search_fields = ("titulo", "descripcion")