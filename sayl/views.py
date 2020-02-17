from django.shortcuts import render
from .services import *
import json
from config.models import Configuraciones
from login.models import CustomUser
from asistencias.models import Asistencia
from app_justificacion.models import Justificacion
from django.utils import timezone


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        agente = get_agente(request.user.legajo)
        config = Configuraciones.objects.last()
        mis_cargos = get_cargos_api(request.user.legajo)
        usuarios = CustomUser.objects.all()
        cant_asistencias_hoy = (Asistencia.objects
                                .filter(fecha_marcaje=timezone.now())
                                .exclude(condicion="Inasistencia Injustificada")
                                .exclude(condicion="Inasistencia Justificada")
                                .count()
                                )
        
        cant_justificacion_hoy = Justificacion.objects.filter(estado='Aprobado', fecha_inicio__lte=timezone.now(), fecha_fin__gte=timezone.now()).count()

        #Obtengo los agentes que marcaron el dia de hoy
        agentes_marcaron = CustomUser.objects.filter(asistencia__fecha_marcaje=timezone.now())
        print("Asis de hoy: ",agentes_marcaron)
        
        #Se obtiene todos los marcajes del dia de hoy para verificar que ya no se aplico la inasistencia:
        inasist_ya_marcados = Asistencia.objects.filter(fecha_marcaje=timezone.now(), condicion__startswith="Inasistencia")

        #Obtengo todos los agentes que no marcaron el dia de hoy
        agentes_sinmarcar = CustomUser.objects.exclude(pk__in=agentes_marcaron)
        print("sinmarcar1: ",agentes_sinmarcar)
        #De los que no marcaron obtengo los que tienen justificaciones activas.
        justs_en_curs = Justificacion.objects.prefetch_related('legajo').filter(legajo__in=agentes_sinmarcar, estado="Aprobado")
        print("Just: ", justs_en_curs)     
        
        #De todos los agentes sin marcar dejo solo los que no tienen justificaciones activas.
        agentes_sinmarcar = agentes_sinmarcar.exclude(justificacion__in=justs_en_curs)
        print("sinmarcar1: ",agentes_sinmarcar)
        cant_sin_marcar = agentes_sinmarcar.count()
        print(agentes_sinmarcar)

        cant_agentes_establecimiento  = Asistencia.objects.filter(condicion="Entrada Válida").filter(condicion="Entrada Fuera de Horario").count()

        context = {'agente':agente, 
                    'config':config, 
                    'mis_cargos':mis_cargos, 
                    'usuarios':usuarios,
                    'cant_asistencias_hoy':cant_asistencias_hoy,
                    'cant_justificacion_hoy':cant_justificacion_hoy,
                    'cant_sin_marcar': cant_sin_marcar,
                    'cant_agentes_establecimiento':cant_agentes_establecimiento
                    }  
        return render(request, 'sayl/index.html', context)
    return render(request, 'sayl/index.html')

def profile(request):
    agente = get_agente(request.user.legajo)
    context = {'agente':agente}
    return render(request, 'sayl/profile.html', context)

def edit_contact(request, pk):
    # user_contact = UserContact.objects.get(pk=pk)
    # if request.method == 'GET':
    #     form = UserContactForm(instance = user_contact)
    # else:
    #     form = UserContactForm(request.POST, instance = user_contact)
    #     print(form.errors)
    #     if form.is_valid():
    #         user_contact = form.save(commit=False)
    #         user_contact.changeReason = 'Modificacion de Contacto'
    #         user_contact.save()
    #     return redirect('index')    
    pass
    #return render(request, 'sayl/editar_contacto.html', {'form':form, 'cargos':cargos})

