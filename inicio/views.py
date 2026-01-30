from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse #este no importa, era para pruebas

# def indice(request):
#     return HttpResponse("Hola 🫠 Estás en la app 'Home'.")

def indice(request):
    contexto= {
        "ahora": timezone.localtime(),
        "temas": ["lechuga","pera","manzana","platano"],
        "modo": "practica", #es el estado
    }
    #render(peticion, DONDE, QUE)
    #DONDE es la ubicacion de la plantilla html
    # QUE son los datos que se enviara a la plantilla y utiliza dentro de 
    return render(request, "inicio/inicio.html", contexto) #esto en vez de https


def acerca(request):
    return render(request, "inicio/acerca.html")

def temario(request):
    return render(request, "inicio/temario.html")

# def pato(request):
#     return HttpResponse("Cuak 🦆")

# def vaca(request):
#     return HttpResponse("Muuu 🐮")