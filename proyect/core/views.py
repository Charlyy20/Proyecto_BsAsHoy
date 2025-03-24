from django.shortcuts import render
from . import models
from django.shortcuts import render, get_object_or_404
from .models import Noticia

def detalle_noticia(request, slug):
    # Obtener la noticia basada en el slug (o lanzar un error 404 si no existe)
    noticia = get_object_or_404(Noticia, slug=slug)
    
    # Pasar la noticia al template
    return render(request, 'core/single-post.html', {'noticia': noticia})

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request,"core/about.html")

def post(request):
    return render(request,"core/single-post.html")

def contact(request):
    return render(request,"core/contact.html")

def category(request):
    return render(request,"core/category.html")



