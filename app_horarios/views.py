from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from edificios.models import Edificio, Provincia
from .forms import DetalleHorarioForm, HorariosFijosForm
from django.contrib import messages
from sayl.services import get_cargos_api
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta
import time
from sayl.utils import dia_de_semana
from login.models import CustomUser
from config.models import Configuraciones
from cargos.models import CargosCache
from sayl.utils import time2timedelta

# Create your views here.

def index(request):
    cargo_actual = CargosCache.objects.get(customuser=request.user, seleccionado=True)
    config = Configuraciones.objects.filter().order_by('-id')[0]
    d_horarios = DetalleHorario.objects.filter(horario__legajo=request.user, horario__cargo=cargo_actual)
    form_detalle_horario = DetalleHorarioForm()
    print(cargo_actual)
    h = Horario.objects.filter(legajo=request.user, cargo=cargo_actual)
    
    #horas_semanales = get_cargos_api(request.user)
    
    #horas_semanales = horas_semanales[0]['horas_dedicacion']
    #agregar porcentaje frente al aula.
    
    #Obtenemos las horas semanales que tiene que cumplir el cargo actual
    
    print(cargo_actual.horas_dedicacion)


    if request.method == 'POST': 
        form_detalle_horario = DetalleHorarioForm(request.POST)   
        print("Error: ", form_detalle_horario.errors)    
        if form_detalle_horario.is_valid():    
            if h.count() > 0:
                print("Existe")
                desde = form_detalle_horario.cleaned_data['desde'] 
                hasta = form_detalle_horario.cleaned_data['hasta']            
                dia = form_detalle_horario.cleaned_data['dia']            
                horario = Horario.objects.get(legajo=request.user,cargo=cargo_actual)
                
                print(type(hasta))
                #hasta = hasta - timedelta(minutes=1)
                #desde = desde + timedelta(minutes=1)
                print("Horarios fijos: ", HorariosFijos.objects.filter(hora_entrada__lte=hasta, hora_salida__gte=desde, agente=request.user))
                if (DetalleHorario.objects.filter(desde__lte=hasta, hasta__gte=desde, dia=dia, horario__legajo=request.user).exists()
                    or HorariosFijos.objects.filter(hora_entrada__lte=hasta, hora_salida__gte=desde, agente=request.user).exists()):
                    messages.error(request, 'Ya existe este horario establecido. Revise los horarios de sus otros cargos')
                else:
                                        
                    detalle_horario = form_detalle_horario.save(commit=False)
                    detalle_horario.horario = horario
                    detalle_horario.save()
            else:
                print("No existe")
                edificio = Edificio.objects.get(pk=1)
                periodo_lectivo = PeriodoLectivo.objects.get(pk=1)
                horario = Horario(edificio=edificio,periodo_lectivo=periodo_lectivo,legajo=request.user, cant_modificaciones=2, cargo=cargo_actual) #SETTINGS -> Parametrizar cant_modif
                horario.save()
                print(horario)
                detalle_horario = form_detalle_horario.save(commit=False)
                detalle_horario.horario = horario
                detalle_horario.save()          
    else:
        horario = Horario.objects.get(legajo=request.user, cargo=cargo_actual) if h.count() > 0 else None

    horas_declaradas = DetalleHorario.objects.select_related('horario').filter(horario=horario)
    total_declarado = timedelta()
    for hora_declarada in horas_declaradas:
        dsd = time2timedelta(hora_declarada.desde)
        hst = time2timedelta(hora_declarada.hasta)
        total_declarado += hst - dsd
        print(hst , "-", dsd, " = ", total_declarado)
    
    total_declarado = '%02d.%02d' % (total_declarado.days*24 + total_declarado.seconds // 3600, ((total_declarado.seconds % 3600) // 60) + (total_declarado.seconds % 60) + total_declarado.microseconds)
    total_declarado = float(total_declarado)
    
    #total_declarado = float(total_declarado.replace(":",".",2))
    print("Total declarado: ", total_declarado)
    porcentaje_frente_aula = (config.porcentaje_frente_aula / 100)
    print("porcentaje", config.porcentaje_frente_aula)
    #Pasamos el timedelta a float
    # secs=total_declarado.seconds #timedelta has everything below the day level stored in seconds
    # minutes = ((secs/60)%60)/60.0
    # hours = secs/3600
    # total_declarado = hours + minutes
    print("Total declarado: ", total_declarado)
    porcentaje_horas = None
    horas_dedicacion =  round(cargo_actual.horas_dedicacion * porcentaje_frente_aula)
    return render(request, 'app_horarios/index.html', {'horario':horario, 'd_horarios':d_horarios, 'form_detalle_horario':form_detalle_horario, 'porcentaje_horas':porcentaje_horas, 'horas_dedicacion':horas_dedicacion, 'declarado_actual':total_declarado, 'config':config})
    


# def modificar_detalle_horario(request, pk):
#     dhorario = DetalleHorario.objects.get(pk=pk)
#     if request.method == 'GET':
#         form = DetalleHorarioForm(instance = dhorario)
#         cargos = get_categorias()
#     else:
#         form = DetalleHorarioForm(request.POST, instance = dhorario)
#         print(form.errors)
#         if form.is_valid():            
#             dhorario = form.save(commit=False)
#             dhorario.changeReason = 'Modificacion de Detalle de Horario'
#             dhorario.save()
#         return redirect('/app_horarios')    
    
#     return render(request, 'app_horarios/agregar_modal.html', {'form':form, 'cargos':cargos})

def eliminar_detalle_horario(request, pk):
    dhorario = DetalleHorario.objects.get(pk=pk)    
    try:
        dhorario.changeReason='Eliminacion de Detalle de Horario'
        dhorario.delete()
    except:
        messages.error(request, 'No se puede eliminar este horario.')
    return redirect('/app_horarios')

def finalizar_declaracion_horarios(request, pk):
    cargo_actual = CargosCache.objects.get(customuser=request.user, seleccionado=True)
    horario = Horario.objects.get(pk=pk, cargo=cargo_actual)
    horario.activo = True
    horario.save()
    return redirect('/app_horarios')

def editar_declaracion_horarios(request, pk):
    horario = Horario.objects.get(pk=pk)
    if horario.cant_modificaciones > 0:
        horario.activo = False
        horario.cant_modificaciones -= 1
        horario.save()
    else:
        mensajito = """Ya no se pueden realizar modificaciones a la declaracion de horarios, 
        por favor para modificar contacte con el supervior de Asistencias y Licencias """
        messages.error(request, mensajito)
    return redirect('/app_horarios')


def horarios_fijos(request):    
    users = CustomUser.objects.filter(cargos_cache__escalafon="NODO", horariosfijos__isnull=True).distinct().order_by('last_name')
    print(users)
    if request.method == "POST":
        form_horario_fijo = HorariosFijosForm(request.POST)

        #De la lista a asignar, traigo cada objeto para asociarlos al horario
        asignar_a = request.POST.getlist('usuarios[]')
        lista_agentes = []
        for agente in asignar_a:
            lista_agentes.append(CustomUser.objects.get(pk=agente))
            
        print(form_horario_fijo.errors)
        if form_horario_fijo.is_valid():
            h_entrada = form_horario_fijo.cleaned_data['hora_entrada']
            hs_a_cumplir = form_horario_fijo.cleaned_data['horas_a_cumplir']
            hs_cumplir = time2timedelta(hs_a_cumplir)
            hora_entrada = time2timedelta(h_entrada)
            hora_salida = hora_entrada + hs_cumplir
            h_salida = (datetime.min + hora_salida).time()
            print("------------")
            print(hora_salida)
            print("------------")
            print(DetalleHorario.objects.filter(desde__lte=h_salida, hasta__gte=h_entrada, horario__legajo=request.user))
            if not(HorariosFijos.objects.filter(hora_entrada=h_entrada, horas_a_cumplir = hs_a_cumplir).exists()):
                if (HorariosFijos.objects.filter(hora_entrada__lte=h_salida, hora_salida__gte=h_entrada, agente__in=lista_agentes).exists()
                    or DetalleHorario.objects.filter(desde__lte=h_salida, hasta__gte=h_entrada, horario__legajo=request.user).exists()):
                    
                    messages.error(request, 'Ya existe este horario establecido.')
                else:
                    print("h_entrada: ", h_entrada)
                    print("h_salida: ", h_salida)
                    print(DetalleHorario.objects.filter(desde__lte=h_salida, hasta__gte=h_entrada, horario__legajo=request.user))
                    
                    horario_fijo = form_horario_fijo.save(commit=False)
                    horario_fijo.hora_salida = h_salida
                    horario_fijo.save()
                    horario_fijo.agente.add(*lista_agentes)
            else:
                horario_fijo = HorariosFijos.objects.get(hora_entrada=h_entrada, horas_a_cumplir = hs_a_cumplir)
                horario_fijo.agente.add(*lista_agentes)
    else:
        config = Configuraciones.objects.filter().order_by('-id')[0]
        print("config: ", config.horas_a_cumplir_default)
        form_horario_fijo = HorariosFijosForm(initial={'horas_a_cumplir': config.horas_a_cumplir_default})
    horarios_fijos = HorariosFijos.objects.all()
    context = {'users':users, 'form_horario_fijo':form_horario_fijo, 'horarios_fijos':horarios_fijos}
    return render(request, 'app_horarios/horarios_fijos.html', context)

def eliminar_horario_fijo(request,pk, pk_agente):    
    hf = HorariosFijos.objects.get(pk=pk)
    hf.agente.remove(pk_agente)
    print("ola: ", hf)
    try:
        # hf.changeReason='Eliminacion de Tipo de Justificacion'
        # hf.delete()
        pass
    except:
        messages.error(request, 'No se puede eliminar el tipo de justificacion')
    return redirect('/app_horarios/horarios_fijos')
