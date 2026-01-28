from django.http import HttpResponse

def indice(request):
    return HttpResponse("Hola 🫠 Estás en la app 'Home'.")

def pato(request):
    return HttpResponse("Cuak 🦆")

def vaca(request):
    return HttpResponse("Muuu 🐮")