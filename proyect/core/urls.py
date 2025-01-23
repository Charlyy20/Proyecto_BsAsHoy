from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("post/", views.post, name="post"),
    path("contact/", views.contact, name="contact"),
    path("category/", views.category, name="category"),
    
]