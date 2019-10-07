from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import JustificacionForm
from .models import Justificacion
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import JustificacionSerializer

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
    justificaciones = Justificacion.objects.select_related('tipo_justificacion','legajo')
    
    return render(request, 'app_justificacion/index_admin.html', {'justificaciones':justificaciones})

def avisar_inasistencia(request):
    form_justificacion = JustificacionForm()
    justificaciones = Justificacion.objects.all()

    if request.method == 'POST':
        form_justificacion = JustificacionForm(request.POST)
        print(form_justificacion.errors)
        if form_justificacion.is_valid():
            just = form_justificacion.save(commit=False)
            just.legajo =  request.user            
            just.save()
            return redirect('avisar_inasistencia')
    else:
        form_justificacion = JustificacionForm()
        


    context = {'form_justificacion':form_justificacion, 'justificaciones':justificaciones}
    return render(request, 'app_justificacion/avisar_inasistencia.html',context)

@csrf_exempt
def justificaciones_list(request, id_justificacion):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        justificaciones = Justificacion.objects.prefetch_related('tipo_justificacion','legajo').filter(pk=id_justificacion)
        serializer = JustificacionSerializer(justificaciones, many=True)
        result = dict()
        result['data'] = serializer.data
        return JSONResponse(result)

