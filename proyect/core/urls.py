from django.urls import path

from . import views

ultra_patterns = [
    path("", views.home),
]