from django.shortcuts import render
from django.conf import settings

from . import models

def home(request):
    banners_base = [
        {
            "titulo": "Banner Ituzaingó",
            "url": f"{settings.MEDIA_URL}banners_clientes/BANNER_ITUZAINGO_.jpg",
        },
        {
            "titulo": "Banner José C. Paz",
            "url": f"{settings.MEDIA_URL}banners_clientes/BANNER_JOSE_C_PAZ_MAYO_2026.jpg",
        },
        {
            "titulo": "Banner Merlo",
            "url": f"{settings.MEDIA_URL}banners_clientes/BANNER_MERLO.jpg",
        },
        {
            "titulo": "Banner Merlo 2",
            "url": f"{settings.MEDIA_URL}banners_clientes/BANNER_MERLO_2.jpg",
        },
        {
            "titulo": "Banner Merlo 3",
            "url": f"{settings.MEDIA_URL}banners_clientes/BANNER_MERLO_3.png",
        },
        {
            "titulo": "Banner General Rodríguez",
            "url": f"{settings.MEDIA_URL}banners_clientes/BANNER_GENERAL_RODRIGUEZ_MAYO_2026.jpeg",
        },
        {
            "titulo": "Banner Morón GIF",
            "url": f"{settings.MEDIA_URL}banners_clientes_gif/BANNER_MORON.gif",
        },
        {
            "titulo": "Banner San Isidro GIF",
            "url": f"{settings.MEDIA_URL}banners_clientes_gif/BANNER_SAN_ISIDRO.gif",
        },
    ]

    banners_home = [
        banners_base[0],
        banners_base[1],
        banners_base[2],
        banners_base[3],
        banners_base[4],
        banners_base[5],
        banners_base[6],
        banners_base[7],
        banners_base[0],
        banners_base[1],
        banners_base[3],
        banners_base[7],
    ]

    banners_filas = [
        banners_home[0:4],
        banners_home[4:8],
        banners_home[8:12],
    ]

    return render(request, "core/index.html", {
        "banners_filas": banners_filas,
    })


def about(request):
    return render(request, "core/about.html")


def post(request):
    return render(request, "core/single-post.html")


def contact(request):
    return render(request, "core/contact.html")


def category(request):
    return render(request, "core/category.html")