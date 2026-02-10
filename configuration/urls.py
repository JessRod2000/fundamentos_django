
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path("home/", include("home.urls")), #le dice que todas las rutas de home.urls con /home
    path("", include("inicio.urls")), #raiz
    path("rutas/", include("rutas.urls")),
    path('admin/', admin.site.urls)
]
