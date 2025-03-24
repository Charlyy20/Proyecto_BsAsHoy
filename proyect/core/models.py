from django.db import models
from django.utils.text import slugify

#Models template de noticia

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
class Noticia(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="noticias")
    link_unico = models.URLField(unique=True, blank=True, null=True)  # Nuevo campo para el link único
    imagen_portada = models.ImageField(upload_to='noticias/imagenes/', blank=True, null=True)
    video = models.FileField(upload_to='noticias/videos/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo