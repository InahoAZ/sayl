from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def index(request):
    tiposjust = TipoJustificacion.objects.all()
    return render(request, 'app_tipojustificacion/index.html', {'tiposjust':tiposjust})

def listado_tjust(request):
    return HttpResponse("Listado de Tipos de Justificaciones")

def detalle_tjust(request, tipo_justificacion_id):
    return HttpResponse("Detalle del Tipo de Justificacion N° %s" % tipo_justificacion_id)

def agregar_tjust(request, tipo_justificacion_id):
    return HttpResponse("Agregar Tipo de Justificacion N° %s" % tipo_justificacion_id)

def eliminar_tjust(request, tipo_justificacion_id):
    return HttpResponse("Eliminar Tipo de Justificacion N° %s" % tipo_justificacion_id)

def modificar_tjust(request, tipo_justificacion_id):
    return HttpResponse("Modificar Tipo de Justificacion N° %s" % tipo_justificacion_id)