from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TipoJustificacion
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# from .serializers import JustificacionSerializer
from .serializers import TipoJustificacionSerializer

from .forms import TipoJustificacionForm
from sayl.services import *

# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@login_required
def index(request):
    tiposjust = TipoJustificacion.objects.all()
    form_tj = TipoJustificacionForm()
    cargos = get_categorias()
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
            tjust = form.save(commit=False)
            tjust.changeReason = 'Creacion de Tipo de Justificacion'
            tjust.save()
            return redirect('index')
    else:
        form = TipoJustificacionForm()        
    
    #return render(request, 'app_tipojustificacion/agregar_modal.html', {'form':form})

def eliminar_tjust(request, tipo_justificacion_id):
    
    tjust = TipoJustificacion.objects.get(id=tipo_justificacion_id)    
    try:
        tjust.changeReason='Eliminacion de Tipo de Justificacion'
        tjust.delete()
    except:
        messages.error(request, 'No se puede eliminar el tipo de justificacion')
    return redirect('/app_tipojustificacion')
    

def modificar_tjust(request, tipo_justificacion_id):
    tjust = TipoJustificacion.objects.get(id=tipo_justificacion_id)
    if request.method == 'GET':
        form = TipoJustificacionForm(instance = tjust)
        cargos = get_categorias()
    else:
        form = TipoJustificacionForm(request.POST, instance = tjust)
        print(form.errors)
        if form.is_valid():
            cargos = None
            tjust = form.save(commit=False)
            tjust.changeReason = 'Modificacion de Tipo de Justificacion'
            tjust.save()
        return redirect('/app_tipojustificacion')    
    
    return render(request, 'app_tipojustificacion/agregar_modal.html', {'form':form, 'cargos':cargos})


@csrf_exempt
def tipos_justificacion_list(request):
    cg = request.GET.get('cargo', None)    
    if request.method == 'GET':
        if cg != 0:
            tipos_justificacion = TipoJustificacion.objects.filter(cargo=cg)
        else:
            tipos_justificacion = TipoJustificacion.objects.all()
        serializer = TipoJustificacionSerializer(tipos_justificacion, many=True)
        
        result = dict()
        result = serializer.data
        return JSONResponse(result)