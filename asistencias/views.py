from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Asistencia, Edificio
from app_justificacion.models import Justificacion
from app_horarios.models import Horario, DetalleHorario
from django.utils import timezone
from datetime import datetime, timedelta, date, time
from django.utils import timezone
from .forms import AsistenciaForm
from login.models import CustomUser
from sayl.utils import dia_de_semana, time2timedelta
from config.models import Configuraciones
from dateutil.parser import parse


# Create your views here.

def index(request):
    asistencias = Asistencia.objects.all()
    context = {'asistencias':asistencias} 
    print(asistencias)
    return render(request,'asistencias/marcajes.html', context)

def simulador_biometrico(request):
    return render(request, 'asistencias/simulador_biometrico.html')

def simular_marcaje(request):
    
    
    #Verifica si el usuario ya registro un marcaje en el dia de hoy:
    ya_marco = Asistencia.objects.filter(fecha_marcaje=timezone.now(), legajo = request.user)
    print(timezone.now().time())

    #Obtiene el dia de la semana del 1 al 7 y lo transforma en un string del tipo Lunes, Martes, etc.
    dia_de_hoy = int(timezone.now().strftime("%w"))
    dia_de_hoy = dia_de_semana(dia_de_hoy)    
    
    #print("mis_horarios: ", mis_horarios)
    
    #Verifico si en el dia de hoy existe algun horario declarado que cumplir:
    if Horario.objects.prefetch_related('detallehorario').filter(legajo=request.user.legajo, activo=True, detallehorario__dia=dia_de_hoy).exists():   
        print("Existe")
        #Como existe, obtengo el horario del agente que realizo el marcaje en el dia de hoy:
        mis_horarios = Horario.objects.get(legajo=request.user.legajo, activo=True, detallehorario__dia=dia_de_hoy)
        #El detalle del horario de hoy:    
        d_horario = DetalleHorario.objects.get(horario=mis_horarios, dia=dia_de_hoy)  

        #Se trae el tiempo de tolerancia configurado
        tiempo_tolerancia = Configuraciones.objects.get(nombre_config="tiempo_tolerancia")

        #Se agrega la tolerancia:
        desde = time2timedelta(d_horario.desde)
        hasta = time2timedelta(d_horario.hasta)
        tiempo_tolerancia = Configuraciones.objects.get(nombre_config="tiempo_tolerancia")
        tiempo_tolerancia = timedelta(minutes=tiempo_tolerancia.valor_config)   
        tol_desde = desde - tiempo_tolerancia
        tol_hasta = hasta + tiempo_tolerancia
        #print(tol_desde, " - ", tol_hasta)
    else:        
        tol_desde = None
        tol_hasta = None
    #print(ya_marco.last().hora_salida)
    #Verifico si ya marco el agente el dia de hoy.
    if not(ya_marco) or (ya_marco.last().hora_salida != None and ya_marco.last().condicion != "Entrada Válida"):
        print("No marco")        

        asistencia = Asistencia()
        asistencia.fecha_marcaje = timezone.now().date()
        asistencia.hora_entrada = timezone.now().time()
        marcaje_desde = time2timedelta(asistencia.hora_entrada)
        
        
        
        if tol_desde != None and marcaje_desde>=tol_desde:   
            asistencia.condicion = "Entrada Válida"
        else:
            asistencia.condicion = "Entrada Fuera de Horario"
        asistencia.legajo = request.user
        ed = Edificio.objects.get(pk=1) #Harcodeada
        asistencia.edificio = ed
        asistencia.save()
        print("redirect 1")
        return redirect('/asistencias/')
    else:
        print("Marco")
        marcaje = Asistencia.objects.filter(fecha_marcaje=timezone.now(), legajo = request.user).last()
        marcaje_hasta = time2timedelta(timezone.now().time())
        if marcaje.hora_salida == None and marcaje.condicion == "Entrada Válida":
            marcaje.hora_salida = timezone.now().time()
            
            #Verifica si la salida fue dentro del horario declarado como salida. (Con cierto tiempo de margen)
            if marcaje_hasta<=tol_hasta:
                marcaje.condicion = "Marcaje Válido"
            else:
                marcaje.condicion = "Salida Fuera de Horario"

            marcaje.save()
        if marcaje.hora_salida == None and marcaje.condicion == "Entrada Fuera de Horario":
            marcaje.hora_salida = timezone.now().time()
            marcaje.condicion = "Marcaje Fuera de Horario"
            marcaje.save()
        print("redirect 2")

    return redirect('/asistencias/')

def corregir_marcaje(request, pk):
    asistencia = Asistencia.objects.get(pk=pk)
    if request.method == 'GET':
        form = AsistenciaForm(instance = asistencia)
    else:
        form = AsistenciaForm(request.POST, instance = asistencia)
        print(form.errors)
        if form.is_valid():
            asist = form.save(commit=False)
            asist.changeReason = 'Correccion de Asistencia'
            asist.save()
        return redirect('index')
    context = {'form_corregir_marcaje': form}
    return render(request, 'asistencias/corregir_marcaje.html', context)

def inasistencia_automatica(request): #FALTA CONTROLAR QUE NO PONGA LA FALTA SI YA SE HIZO
    #asist_dehoy = Asistencia.objects.filter(fecha_marcaje=timezone.now(), condicion="Marcaje Válido") 
    
    #Obtengo los agentes que marcaron el dia de hoy
    agentes_marcaron = CustomUser.objects.filter(asistencia__fecha_marcaje=timezone.now())
    print("Asis de hoy: ",agentes_marcaron)
    
    #Se obtiene todos los marcajes del dia de hoy para verificar que ya no se aplico la inasistencia:
    inasist_ya_marcados = Asistencia.objects.filter(fecha_marcaje=timezone.now(), condicion__startswith="Inasistencia")

    #Obtengo todos los agentes que no marcaron el dia de hoy
    agentes_sinmarcar = CustomUser.objects.exclude(pk__in=agentes_marcaron, asistencia__in=inasist_ya_marcados)
    print(agentes_sinmarcar)
    #De los que no marcaron obtengo los que tienen justificaciones activas.
    justs_en_curs = Justificacion.objects.prefetch_related('legajo').filter(legajo__in=agentes_sinmarcar, estado="Aprobado")
    print("Just: ", justs_en_curs)
    


    #De todos los agentes sin marcar dejo solo los que no tienen justificaciones activas.
    agentes_sinmarcar = CustomUser.objects.exclude(justificacion__in=justs_en_curs)
    print("nueva lista: ", agentes_sinmarcar)

    for agente_sinmarcar in agentes_sinmarcar:
        #por cada agente sin marcar que no tiene una justificacion le registro una inasistencia.
        if not(Asistencia.objects.filter(legajo=agente_sinmarcar, fecha_marcaje=timezone.now()).exists()):
            newinasist = Asistencia() #Si ya se, se deberia llamar marcajes no asistencia xd
            newinasist.fecha_marcaje = timezone.now()
            newinasist.legajo = agente_sinmarcar
            newinasist.hora_entrada = '00:00'
            newinasist.hora_salida = '00:00'
            newinasist.condicion = 'Inasistencia Injustificada'
            #Edificio harcodeado
            newinasist.edificio = Edificio.objects.get(pk=1)
            newinasist.save()
    
    
    for j_en_curs in justs_en_curs:       

        if timezone.now().date() >= j_en_curs.fecha_inicio and timezone.now().date() <= j_en_curs.fecha_fin:
            print("Esta en la fecha")
            if not(Asistencia.objects.filter(legajo=j_en_curs.legajo, fecha_marcaje=timezone.now()).exists()):
                newinasistjust = Asistencia()
                newinasistjust.fecha_marcaje = timezone.now()
                newinasistjust.legajo = j_en_curs.legajo
                newinasistjust.hora_entrada = '00:00'
                newinasistjust.hora_salida = '00:00'
                newinasistjust.condicion = 'Inasistencia Justificada'
                #Edificio harcodeado
                newinasistjust.edificio = Edificio.objects.get(pk=1)
                newinasistjust.save()

    return redirect('/asistencias/')
    

