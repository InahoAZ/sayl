from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Asistencia, Edificio
from app_justificacion.models import Justificacion
from app_horarios.models import Horario, DetalleHorario, HorariosFijos
from django.utils import timezone
from datetime import datetime, timedelta, date, time
from django.utils import timezone
from .forms import AsistenciaForm
from login.models import CustomUser
from sayl.utils import dia_de_semana, time2timedelta, dia_de_mes
from config.models import Configuraciones
from dateutil.parser import parse
from calendario.models import Feriado
from cargos.models import CargosCache
from notify.signals import notify



# Create your views here.

def index(request):
    config = Configuraciones.objects.filter().order_by('-id')[0]
    print("A ber")
    if request.user.is_superuser:
        asistencias = Asistencia.objects.all()
    else:
        asistencias = Asistencia.objects.filter(legajo=request.user)
    
    context = {'asistencias':asistencias, 'config':config} 
    print(config)
    return render(request,'asistencias/marcajes.html', context)

def simulador_biometrico(request):
    return render(request, 'asistencias/simulador_biometrico.html')

def simular_marcaje(request): #Tengo que pensarlo como la realidad del biometrico no se van a loguear para marcar. (Cambiar request.user... a el usuario que le mande el biometrico)
    
    print("SIMULA3")
    
    #Verifica si el usuario ya registro un marcaje en el dia de hoy:
    ya_marco = Asistencia.objects.filter(fecha_marcaje=timezone.now(), legajo = request.user)
    print(timezone.now().time())

    #Obtiene el dia de la semana del 1 al 7 y lo transforma en un string del tipo Lunes, Martes, etc.
    dia_de_hoy = int(timezone.now().strftime("%w"))
    dia_de_hoy = dia_de_semana(dia_de_hoy)   
    print(dia_de_hoy) 
    corresponde_horario = None
    #Se trae el tiempo de tolerancia configurado
    tt = Configuraciones.objects.filter().order_by('-id')[0]
    mtol = tt.tiempo_tolerancia
    
    #tiempo_tolerancia = Configuraciones.objects.get(nombre_config="tiempo_tolerancia")
    tt = timedelta(minutes=int(mtol))   
    td = timezone.now() - tt
    th = timezone.now() + tt
    print("hf: ", td)
    print("hf: ", th)
    #print("mis_horarios: ", mis_horarios)
    print(Horario.objects.filter(legajo=request.user, activo=True, detallehorario__dia=dia_de_hoy))
    #Verifico si en el dia de hoy existe algun horario declarado que cumplir:
    cargo_actual = CargosCache.objects.get(customuser=request.user, seleccionado=True)
    if Horario.objects.filter(legajo=request.user, activo=True, detallehorario__dia=dia_de_hoy, cargo=cargo_actual).exists():   
        print("Existe")
        
        #Como existe, obtengo el horario del agente que realizo el marcaje en el dia de hoy:
        
        print(cargo_actual)
        mis_horarios = Horario.objects.get(legajo=request.user, activo=True, detallehorario__dia=dia_de_hoy, cargo=cargo_actual)
        print(mis_horarios)
        #El detalle del horario de hoy:    
        d_horario = DetalleHorario.objects.get(horario=mis_horarios, dia=dia_de_hoy)  
        
        #Se trae el tiempo de tolerancia configurado
        tiempo_tolerancia = Configuraciones.objects.filter().order_by('-id')[0]
        minutos_tol = tiempo_tolerancia.tiempo_tolerancia
        tiempo_tolerancia = None
        #Se agrega la tolerancia:
        desde = time2timedelta(d_horario.desde)
        hasta = time2timedelta(d_horario.hasta)
        #tiempo_tolerancia = Configuraciones.objects.get(nombre_config="tiempo_tolerancia")
        tiempo_tolerancia = timedelta(minutes=int(minutos_tol))   
        tol_desde = desde - tiempo_tolerancia
        tol_hasta = hasta + tiempo_tolerancia
        print(tol_desde, " - ", tol_hasta)
        corresponde_horario = d_horario
    else:
        #Si no hay horario declarado (doc), se verifica si no hay un horario fijo (nodoc)
        tiempo_tolerancia = Configuraciones.objects.filter().order_by('-id')[0]
        print(HorariosFijos.objects.filter(agente=request.user, hora_entrada__lte=timezone.now(), hora_salida__gte=timezone.now()))
        marcaje_tol = timezone.now() + timedelta(minutes=int(tiempo_tolerancia.tiempo_tolerancia))
        marcaje_tol_hasta = timezone.now() - timedelta(minutes=int(tiempo_tolerancia.tiempo_tolerancia))
        print(marcaje_tol)
        if HorariosFijos.objects.filter(agente=request.user, hora_entrada__lte=marcaje_tol, hora_salida__gte=marcaje_tol_hasta).exists():
            print("Es horario fijo")
            horario_fijo = HorariosFijos.objects.get(agente=request.user)   
            
            tiempo_tolerancia = tiempo_tolerancia.tiempo_tolerancia
            #Se agrega la tolerancia:
            desde = time2timedelta(horario_fijo.hora_entrada)
            hasta = time2timedelta(horario_fijo.hora_salida)

            tiempo_tolerancia = timedelta(minutes=int(tiempo_tolerancia))   
            tol_desde = desde - tiempo_tolerancia
            tol_hasta = hasta + tiempo_tolerancia
            print("hf: ", tol_desde)
            print("hf: ", tol_hasta)


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
        dt = datetime.now()
        dt = dt.replace(hour=0, minute=0, second=0, microsecond=0) # Returns a copy
        mes = dia_de_mes(dt.month)
        

        if Feriado.objects.filter(nro_dia = dt.day, mes=mes).exists():
            newinasist.condicion = 'Dia no Laborable'
        else:
            print("Tol DESDE      ->", tol_desde)
            print("marco en: ", marcaje_desde)
            if tol_desde != None and marcaje_desde>=tol_desde:   
                asistencia.condicion = "Entrada Válida"
            else:
                asistencia.condicion = "Entrada Fuera de Horario"
        asistencia.legajo = request.user
        ed = Edificio.objects.get(pk=1) #Harcodeada
        asistencia.edificio = ed

        if Justificacion.objects.filter(fecha_inicio__lte=timezone.now(), fecha_fin__gte=timezone.now(), legajo=request.user).exists():
            just = Justificacion.objects.get(fecha_inicio__lte=timezone.now(), fecha_fin__gte=timezone.now(), legajo=request.user)
            
            just.estado = "Anulado por Marcaje"
            just.save()

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
            if tol_hasta != None and marcaje_hasta<=tol_hasta:
                marcaje.condicion = "Marcaje Válido"
            else:
                #Aca iria la logica de las horas a favor
                #if DetalleHorario.objects.filter(horario__legajo=request.user, dia=dia_de_hoy).exclude(desde__gte=timezone.now()).order_by('-hasta').exists():

                #     print("Arnold: ",DetalleHorario.objects.filter(horario__legajo=request.user, dia=dia_de_hoy).exclude(desde__gte=timezone.now()).order_by('-hasta')[0])
                #     horario_cercano = DetalleHorario.objects.filter(horario__legajo=request.user, dia=dia_de_hoy).exclude(desde__gte=timezone.now()).order_by('-hasta')[0]
                #     print(tol_desde, "---", tol_hasta)
                #     marcaje.hora_salida = horario_cercano.hasta
                #     marcaje.condicion = "Marcaje Válido"
                #     Asistencia.objects.create(fecha_marcaje=timezone.now(), hora_entrada = horario_cercano.hasta, hora_salida=timezone.now().time(), condicion="Horas a Favor", edificio_id=1, legajo=request.user)
                # else:
                #     marcaje.condicion = "Salida Fuera de Horario"
                
                #Hardcodeada de emergencia. MAÑANA PRESENTO CABEZA
                marcaje.condicion = "Marcaje Válido"

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
            asist.changeReason = 'Correccion de Marcaje'
            notify.send(request.user, recipient=asist.legajo, actor=request.user, verb='ha corregido su marcaje', actor_url="/asistencias")
            asist.save()
        return redirect('/asistencias/')
    context = {'form_corregir_marcaje': form}
    return render(request, 'asistencias/corregir_marcaje.html', context)

def inasistencia_automatica(request):
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

    #Obtengo los agentes que tienen horarios en el dia que se coloca la inasistencia.
    diaa = timezone.now()
    diaa = diaa.strftime("%w")
    diaa = dia_de_semana(int(diaa))
    print(diaa)
    horarios_hoy = DetalleHorario.objects.filter(dia=diaa)
    print(horarios_hoy)
    print("-->", Horario.objects.filter(detallehorario__in=horarios_hoy))
    h =  Horario.objects.filter(detallehorario__in=horarios_hoy)
    agentes_sinmarcar = agentes_sinmarcar.filter(Q(horario__in=h) | Q(horariosfijos__isnull=False))
    print("xd; ", agentes_sinmarcar)
    


    for agente_sinmarcar in agentes_sinmarcar:
        #por cada agente sin marcar que no tiene una justificacion le registro una inasistencia.
        if not(Asistencia.objects.filter(legajo=agente_sinmarcar, fecha_marcaje=timezone.now()).exists()):
            
            dt = datetime.now()
            dt = dt.replace(hour=0, minute=0, second=0, microsecond=0) # Returns a copy
            mes = dia_de_mes(dt.month)
            print("fechona: ",dt)
            print("fechona: ",mes)
            newinasist = Asistencia() #Si ya se, se deberia llamar marcajes no asistencia xd
            newinasist.fecha_marcaje = timezone.now()
            newinasist.legajo = agente_sinmarcar
            newinasist.hora_entrada = '00:00'
            newinasist.hora_salida = '00:00'
            if Feriado.objects.filter(nro_dia = dt.day, mes=mes).exists():
                newinasist.condicion = 'Dia no Laborable'
            else:               
                newinasist.condicion = 'Inasistencia Injustificada'
                notify.send(request.user, recipient=agente_sinmarcar, actor=agente_sinmarcar, verb='obtuvo una Inasistencia Injustificada', actor_url="/asistencias")
                
            
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

    #Para los agentes que marcaron solo una vez, se le coloca una inconsistencia
    inconsistentes = Asistencia.objects.filter(hora_salida=None)
    for inconsistente in inconsistentes:
        inconsistente.condicion="Inconsistencia de Marcaje"
        notify.send(request.user, recipient=inconsistente.legajo, actor=inconsistente.legajo, verb='obtuvo una Inconsistencia de Marcaje', actor_url="/asistencias")
        inconsistente.save()
    print("INCONSISTENTES: ", inconsistentes)

    return redirect('/asistencias/')
    

