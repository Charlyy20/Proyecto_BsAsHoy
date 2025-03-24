from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'core'

urlpatterns = [
    # Otras URLs...
    path('noticia/<slug:slug>/', views.detalle_noticia, name='detalle_noticia'),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("post/", views.post, name="post"),
    path("contact/", views.contact, name="contact"),
    path("category/", views.category, name="category"),
    
]

