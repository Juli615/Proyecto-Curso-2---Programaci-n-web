from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#Importar modelo
from .models import Auto

# Create your views here.
def index(request):
    #Consultar listado de registros de base de datos
    lista_autos = Auto.objects.all()
    template = loader.get_template("index.html")
    #Agregar autos al contexto del template
    context = {"autos":lista_autos}
    return HttpResponse(template.render(context,request))

def vista_detalle(request, id_auto):
    #Consultar el registro en base de datos
    detalle_auto = Auto.objects.get(id = id_auto)
    #Obtener template
    template = loader.get_template("detail.html")
    #Agregar los datos del registro al contexto del template
    context = {"auto":detalle_auto}
    return HttpResponse(template.render(context,request))