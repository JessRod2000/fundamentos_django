from django.urls import path
from . import views #de inicio . trae a views.py

urlpatterns = [
    path("", views.indice, name="rutas_indice"),
    path("ayuda/",views.ayuda ,name="rutas_ayuda"),
    path("hora/",views.hora_actual,name="rutas_hora"),

]

urlpatterns += [
    path("hola/", views.hola, name="rutas_hola"),
    path("hola/<str:name>/", views.hola_nombre, name="rutas_hola_nombre"),
    path("suma/<int:a>/<int:b>/", views.suma, name="rutas_suma"),
]

urlpatterns += [
    path("buscar/", views.buscar, name="rutas_buscar"),
]

urlpatterns += [
    path("metodo/", views.metodo, name="rutas_metodo"),
]

urlpatterns += [
    path("api/estado/", views.api_estado, name="rutas_api_estado"),
]

urlpatterns += [
    path("age/<int:age>/", views.edad, name="rutas_edad"),
]

urlpatterns += [
    path("par-impar/<int:n>/", views.par_impar, name="par-impar"),
]