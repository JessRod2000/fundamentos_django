from django.urls import path
from . import views #de inicio . trae a views.py

urlpatterns = [
    #1 el nombre,2 la vista y luego llamamos a su funcion, 3 
    #path("/home", views.indice, name="indice"),
    path("", views.indice, name="inicio"),  # ✅ raíz => inicio
    #path("acerca/", views.acerca, name="acerca"),
    #path("temario/", views.temario, name="temario"),
    
    path("pato",views.pato, name="patito"), #para acceder aqui es /home/pato
    path("vaca",views.vaca, name='vaquita')
]