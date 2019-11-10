from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import JustificacionForm
from .models import Justificacion
from app_tipojustificacion.models import TipoJustificacion
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import JustificacionSerializer
from django.contrib import messages
import inflect

# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



def index(request):
    justificaciones = Justificacion.objects.exclude(estado='Aprobado').exclude(estado='Rechazado')
    
    return render(request, 'app_justificacion/index_admin.html', {'justificaciones':justificaciones})

def avisar_inasistencia(request):
    form_justificacion = JustificacionForm()
    justificaciones = Justificacion.objects.filter(legajo=request.user)
    
    #print(justificaciones)
    usuario_actual = request.user
    cargos = usuario_actual.get_cargos()

    if request.method == 'POST':
        form_justificacion = JustificacionForm(request.POST)
        #print(request.user.legajo)
        if form_justificacion.is_valid():
            just = form_justificacion.save(commit=False)
            #print(just.tipo_justificacion)
            #Cuenta la cantidad de licencias que pidio el usuario de ese tipo.
            cantjustificacion = Justificacion.objects.filter(tipo_justificacion=just.tipo_justificacion, legajo=request.user).count()
            
            just.legajo =  request.user
            just.changeReason = 'Aviso de Inasistencia'
            #Pregunta si la cantidad que pidio no supera el limite.
            if cantjustificacion <= just.tipo_justificacion.cant_mes:
                just.save()
            else:
                messages.error(request, 'Has ocupado todas tus justificaciones de este tipo por este mes')
            return redirect('avisar_inasistencia')
    else:
        form_justificacion = JustificacionForm()
        


    context = {
        'form_justificacion':form_justificacion, 
        'justificaciones':justificaciones,
        'cargos_user':cargos,
        }
    return render(request, 'app_justificacion/avisar_inasistencia.html',context)

def cancelar_aviso(request, pk):
    aviso = Justificacion.objects.get(pk=pk)    
    try:
        aviso.delete()
    except:
        messages.error(request, 'No se puede eliminar el tipo de justificacion')
    return redirect('/app_justificacion/avisar_inasistencia')

def aprobar_just(request, pk):
    justificacion = Justificacion.objects.filter(pk=pk).update(estado='Aprobado')
    return redirect('/app_justificacion')

def rechazar_just(request, pk):
    justificacion = Justificacion.objects.filter(pk=pk).update(estado='Rechazado')
    return redirect('/app_justificacion')

def justificaciones_encurso(request):
    just_encurso = Justificacion.objects.filter(estado="Aprobado").order_by('fecha_solicitud')
    context = {'just_encurso': just_encurso}
    return render(request, 'app_justificacion/justificaciones_encurso.html', context)

    

@csrf_exempt
def justificaciones_list(request, pk):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        justificaciones = Justificacion.objects.prefetch_related('tipo_justificacion', 'legajo').filter(pk=pk)
        serializer = JustificacionSerializer(justificaciones, many=True)
        result = dict()
        result = serializer.data
        #print("No ta")
        return JSONResponse(result)



