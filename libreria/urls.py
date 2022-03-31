from django import views
from django.urls import URLPattern,path
from . import views
 

urlpatterns = [
    path('',views.inicio,name="inicio"),
    path('index',views.index,name="index"),
    path('nombre/<nom>/<int:edad>',views.mostrarnombre,name="imprimenombre"),
    path('info',views.informacion,name="info"),
    path('info2',views.informacion2),
    path('enviar',views.enviar,name="enviar"),
    path('crearContacto',views.crearContacto,name="crearContacto"),
    path('contactos',views.contactos,name="contactos"),
]
