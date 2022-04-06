from django.http import HttpResponse
from django.shortcuts import render
from ast import Return



def inicio(request):
  return HttpResponse("<H1>HOLA MUNDO desde el itp</H1>")

  
def index(request):
    return render(request,'pagina/index.html')


def mostrarnombre(request,nom,edad):
    return HttpResponse("<h1>Hola tu nombre es %s y tu edad es de %s </h1>" %(nom,edad))

def informacion(request):
 return render(request,'pagina/info.html')

def informacion2(request):
     return render(request,'pagina/info2.html')
 
def crearContacto(request):
     return render(request,'contactos/crearContacto.html')

def editarContacto(request):
     return render(request,'contactos/editarContacto.html')

def contactos(request):
     return render(request,'contactos/indexContactos.html')

def enviar(request):
    if(request.POST):
        recibedatos = request.POST.dict()
        nombre = recibedatos.get("nombre")  
        edad = recibedatos.get("edad")   
    return HttpResponse(" Hola tu  nombre es %s y tu edad es %s <BR> <a  class='btn btn-primary' href='informacioncontacto' role='button'>Regresar</a>" %(nombre,edad))


