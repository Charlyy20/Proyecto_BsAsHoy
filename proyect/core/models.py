from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.from django.db import models
class BannerCliente(models.Model):
    titulo = models.CharField(max_length=150)
    cliente = models.CharField(max_length=150, blank=True, null=True)
    imagen = models.ImageField(upload_to="banners_clientes/")
    url_destino = models.URLField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Banner de cliente"
        verbose_name_plural = "Banners de clientes"
        ordering = ["-creado"]

    def __str__(self):
        return self.titulo

class BannerClienteGif(models.Model):
    titulo = models.CharField(max_length=150)
    cliente = models.CharField(max_length=150, blank=True, null=True)
    archivo = models.FileField(
        upload_to="banners_clientes_gif/",
        validators=[FileExtensionValidator(allowed_extensions=["gif"])]
    )
    url_destino = models.URLField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Banner GIF de cliente"
        verbose_name_plural = "Banners GIF de clientes"
        ordering = ["-creado"]

    def __str__(self):
        return self.titulo

class FotoNoticia(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to="fotos_noticias/")
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Foto de noticia"
        verbose_name_plural = "Fotos de noticias"
        ordering = ["-creado"]

    def __str__(self):
        return self.titulo


class VideoMp4(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    archivo = models.FileField(
        upload_to="videos/",
        validators=[FileExtensionValidator(allowed_extensions=["mp4"])]
    )
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Video MP4"
        verbose_name_plural = "Videos MP4"
        ordering = ["-creado"]

    def __str__(self):
        return self.titulo