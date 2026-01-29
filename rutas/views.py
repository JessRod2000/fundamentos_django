from django.http import HttpResponse, JsonResponse
from django.utils import timezone

def indice(request):
    return HttpResponse("✅ Laboratorio de rutas activo. Ve a /rutas/ayuda/")

def ayuda(request):
    return HttpResponse(
        "Rutas disponibles: /rutas/hola/, /rutas/hola//, "
        "/rutas/suma///, /rutas/buscar/?q=..., /rutas/api/estado/"
    )

def hora_actual(request):
    ahora = timezone.localtime()
    return HttpResponse(f"🕒 Hora local: {ahora:%Y-%m-%d %H:%M:%S}")

def hola(request):
    return HttpResponse("Hola 👋 persona sin NOMBRE!")

def hola_nombre(request, name):
    return HttpResponse(f"Hola, {name.upper()} 👋")

def suma(request, a, b):
    return HttpResponse(f"Resultado: {a} + {b} = {a + b}")

def buscar(request):
    # q es un query de consulta
    q = request.GET.get("q", "").strip()
    if not q:
        return HttpResponse(" Dejaste vacía la consulta❗ Envía un query: /rutas/buscar/?q=django")
    return HttpResponse(f"🔎 Buscando: {q}")

def metodo(request):
    if request.method == "GET":
        return HttpResponse("Estás usando GET ✅")
    elif request.method == "POST":
        return HttpResponse("Estás usando POST ✅")
    else:
        return HttpResponse(f"Método no manejado: {request.method}", status=405)

def api_estado(request):
    data = {
        "estado": "ok",
        "app": "rutas",
        "ruta": request.path,
        "metodo": request.method,
    }
    return JsonResponse(data)

def edad(request, age):
    if age < 0 or age > 120:
        return HttpResponse(f"Edad inválida: {age}\nEs imposible que tengas esa edad", status=400)
    return HttpResponse(f"Edad válida: {age}")

def par_impar(request, n):
    if n % 2 == 0:
        return HttpResponse(f"El número {n} es PAR")
    return HttpResponse(f"El número {n} es IMPAR")