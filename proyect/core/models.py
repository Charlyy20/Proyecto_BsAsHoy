from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from urllib.parse import urlparse, parse_qs
# Create your models here.from django.db import models


def validar_max_500kb(archivo):
    limite_bytes = 500 * 1024

    if archivo.size > limite_bytes:
        raise ValidationError(
            f"El archivo no puede superar los 500 KB. "
            f"El archivo actual pesa {archivo.size / 1024:.2f} KB."
        )

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


class VideoExterno(models.Model):
    PLATAFORMAS = [
        ("youtube", "YouTube"),
        ("instagram", "Instagram"),
        ("tiktok", "TikTok"),
        ("vimeo", "Vimeo"),
        ("otro", "Otro"),
    ]

    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True, null=True)
    plataforma = models.CharField(max_length=20, choices=PLATAFORMAS, default="youtube")
    url_video = models.URLField()
    miniatura = models.ImageField(
        upload_to="miniaturas_videos/",
        blank=True,
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["jpg", "jpeg", "png", "webp"]),
            validar_max_500kb,
        ]
    )
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Video externo"
        verbose_name_plural = "Videos externos"
        ordering = ["-creado"]

    def __str__(self):
        return self.titulo

    def obtener_youtube_id(self):
        url_parseada = urlparse(self.url_video)

        if url_parseada.netloc in ["www.youtube.com", "youtube.com"]:
            query_params = parse_qs(url_parseada.query)
            return query_params.get("v", [None])[0]

        if url_parseada.netloc == "youtu.be":
            return url_parseada.path.strip("/")

        if "youtube.com" in url_parseada.netloc and "/shorts/" in url_parseada.path:
            return url_parseada.path.split("/shorts/")[1].split("/")[0]

        return None

    @property
    def embed_url(self):
        if self.plataforma == "youtube":
            youtube_id = self.obtener_youtube_id()

            if youtube_id:
                return f"https://www.youtube.com/embed/{youtube_id}"

        return self.url_video

    @property
    def miniatura_url(self):
        if self.miniatura:
            return self.miniatura.url

        if self.plataforma == "youtube":
            youtube_id = self.obtener_youtube_id()

            if youtube_id:
                return f"https://img.youtube.com/vi/{youtube_id}/hqdefault.jpg"

        return None