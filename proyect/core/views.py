from django.shortcuts import render

from . import models

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