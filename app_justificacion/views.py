from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import JustificacionForm
from .models import Justificacion
from login.models import CustomUser
from app_tipojustificacion.models import TipoJustificacion
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import JustificacionSerializer
from django.contrib import messages
from mensajeria.views import mandar_whatsapp, mandar_mail
import inflect
from datetime import datetime, timedelta
from sayl.utils import date2timedelta, daterange
from asistencias.models import Asistencia

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
    justificaciones = Justificacion.objects.exclude(estado='Aprobado').exclude(estado='Rechazado').exclude(estado='Anulado por Marcaje')
    
    if request.method == 'POST':
        pk = request.POST.get('id_just')
        observacion = request.POST.get('observacion')
        justificacion = Justificacion.objects.filter(pk=pk).update(observaciones_supervisor=observacion)
        if "btn-aprobar" in request.POST:
            print("QUE LE PASAAAA")
            justificacion = Justificacion.objects.get(pk=pk)
            print(justificacion.fecha_inicio, " - ", justificacion.fecha_fin)
            for single_date in daterange(justificacion.fecha_inicio, justificacion.fecha_fin):
                if Asistencia.objects.filter(legajo=request.user, fecha_marcaje=single_date, condicion='Inasistencia Injustificada').exists():
                    print("Corregir")
                    Asistencia.objects.filter(legajo=request.user, fecha_marcaje=single_date, condicion='Inasistencia Injustificada').update(condicion='Inasistencia Justificada')
            justificacion = Justificacion.objects.filter(pk=pk).update(estado='Aprobado')   
        if "btn-rechazar" in request.POST:
            justificacion = Justificacion.objects.filter(pk=pk).update(estado='Rechazado')

    return render(request, 'app_justificacion/index_admin.html', {'justificaciones':justificaciones})

def avisar_inasistencia(request):
    form_justificacion = JustificacionForm()
    justificaciones = Justificacion.objects.filter(legajo=request.user)
    users = CustomUser.objects.all().order_by('last_name')
    
    #print(justificaciones)
    usuario_actual = request.user
    cargos = usuario_actual.get_cargos()

    if request.method == 'POST':
        form_justificacion = JustificacionForm(request.POST)
        avisar_a = request.POST.getlist('usuarios[]')        
        print(avisar_a)
        #print(request.user.legajo)
        if form_justificacion.is_valid():       
            desde = form_justificacion.cleaned_data['fecha_inicio'] 
            hasta = form_justificacion.cleaned_data['fecha_fin'] 
            tj = Justificacion.objects.filter(fecha_inicio__lte=hasta, fecha_fin__gte=desde, legajo=request.user)
            print(tj)
            if Justificacion.objects.filter(fecha_inicio__lte=hasta, fecha_fin__gte=desde, legajo=request.user).exists():
                messages.error(request, 'Ya existe alguna solicitud de justificacion en las fechas establecidas. Compruebe que otra justificacion no ocupe algun dia en el rango de fechas seleccionado')
                print(tj)
            else:
                #print(just.tipo_justificacion)
                just = form_justificacion.save(commit=False)
                #Cuenta la cantidad de licencias que pidio el usuario de ese tipo. (MAL)
                cantjustificacion = Justificacion.objects.filter(tipo_justificacion=just.tipo_justificacion, legajo=request.user).count()
                just.legajo =  request.user
                just.changeReason = 'Aviso de Inasistencia'

                #Calcular cantidad de licencias segun rango de dias (BIEN)
                justificaciones = Justificacion.objects.filter(tipo_justificacion=just.tipo_justificacion, legajo=request.user)
                
                print("ENTRO EN EL FOR")
                cant_dias_justificaciones = 0
                #print(cant_justificacion)
                for justificacion in justificaciones:
                    hst = justificacion.fecha_fin
                    dsd = justificacion.fecha_inicio
                    cant_justificaciones = hst - dsd
                    cant_dias_justificaciones += cant_justificaciones.days + 1 #se suma uno porque la diferencia me da un dia menos
                    print("ASFLKASJFLJ ", cant_dias_justificaciones)
                cant_dias_justificaciones += (just.fecha_fin - just.fecha_inicio).days + 1    
                print("ASFLKASJFLJ x2 ", cant_dias_justificaciones)
                #Pregunta si la cantidad que pidio no supera el limite.
                print("Cant al año permitidas: ", just.tipo_justificacion.cant_año)
                print("cant que hay: ", cant_dias_justificaciones)
                if cant_dias_justificaciones <= just.tipo_justificacion.cant_año:
                    
                    #Armado del mensaje predeterminado de Aviso de Inasistencia.
                    motivo = form_justificacion.cleaned_data['tipo_justificacion']
                    motivo = motivo.motivo
                    desde = form_justificacion.cleaned_data['fecha_inicio']
                    hasta = form_justificacion.cleaned_data['fecha_fin']
                    desde = desde.strftime("%d/%m/%Y")
                    hasta = hasta.strftime("%d/%m/%Y")

                    mensaje = request.user.first_name + " "
                    mensaje += request.user.last_name
                    mensaje += " ha notificado que se ausentara por: " + motivo           
                    
                    mensaje += " desde: " + desde
                    mensaje += " hasta: " + hasta
                    
                    if request.user.suscripto_telefono:             
                        mandar_whatsapp(avisar_a, mensaje)
                    if request.user.suscripto_mail:
                        print("Sus mail")
                        mandar_mail(avisar_a, "Sobre Aviso de Inasistencia", mensaje)
                    just.save()
                else:
                    messages.error(request, 'Has ocupado todas tus justificaciones de este tipo por este mes o tu solicitud excede la cantidad de dias permitidos')
                return redirect('avisar_inasistencia')
    else:
        form_justificacion = JustificacionForm()
        


    context = {
        'form_justificacion':form_justificacion, 
        'justificaciones':justificaciones,
        'cargos_user':cargos,
        'users':users,
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
    print("QUE LE PASAAAA")
    justificacion = Justificacion.objects.filter(pk=pk)
    print(justificacion.fecha_inicio, " - ", justificacion.fecha_fin)
    for single_date in daterange(justificacion.fecha_inicio, justificacion.fecha_fin):
        print("---> ", single_date)
    # if Asistencia.objects.filter(legajo=request.user, fecha_marcaje=):

    # justificacion = Justificacion.objects.filter(pk=pk).update(estado='Aprobado')
    
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



