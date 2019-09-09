from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Inicio Gestionar Justificaciones")

def listado_tjust(request):
    return HttpResponse("Listado de Tipos de Justificaciones")

def detalle_tjust(request, tipo_justificacion_id):
    return HttpResponse("Detalle del Tipo de Justificacion N° %s" % tipo_justificacion_id)

def agregar_tjust(request):
    return HttpResponse("Agregar Tipo de Justificacion")

def eliminar_tjust(request, tipo_justificacion_id):
    return HttpResponse("Eliminar Tipo de Justificacion N° %s" % tipo_justificacion_id)

def modificar_tjust(request, tipo_justificacion_id):
    return HttpResponse("Modificar Tipo de Justificacion N° %s" % tipo_justificacion_id)