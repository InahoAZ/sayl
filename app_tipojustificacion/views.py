from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import TipoJustificacionForm

# Create your views here.


def index(request):
    tiposjust = TipoJustificacion.objects.all()
    form_tj = TipoJustificacionForm()
    if request.method == 'POST' and request.POST['accion'] == 'add':        
        agregar_tjust(request)
    return render(request, 'app_tipojustificacion/index.html', {'tiposjust':tiposjust, 'form_tj':form_tj})

def listado_tjust(request):
    return HttpResponse("Listado de Tipos de Justificaciones")

def detalle_tjust(request, tipo_justificacion_id):
    return HttpResponse("Detalle del Tipo de Justificacion N° %s" % tipo_justificacion_id)

def agregar_tjust(request):
    if request.method == 'POST':
        form = TipoJustificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TipoJustificacionForm()        
    
    #return render(request, 'app_tipojustificacion/agregar_modal.html', {'form':form})

def eliminar_tjust(request, tipo_justificacion_id):
    tjust = TipoJustificacion.objects.get(id=tipo_justificacion_id)    
    tjust.delete()
    return redirect('index')
    

def modificar_tjust(request, tipo_justificacion_id):
    tjust = TipoJustificacion.objects.get(id=tipo_justificacion_id)
    if request.method == 'GET':
        form = TipoJustificacionForm(instance = tjust)
    else:
        form = TipoJustificacionForm(request.POST, instance = tjust)
        if form.is_valid():
            form.save()
        return redirect('index')    
    
    return render(request, 'app_tipojustificacion/agregar_modal.html', {'form':form})