from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Asistencia
from django.utils import timezone
import datetime
from .forms import AsistenciaForm
from login.models import CustomUser


# Create your views here.

def index(request):
    asistencias = Asistencia.objects.all()
    context = {'asistencias':asistencias}
    return render(request,'asistencias/marcajes.html', context)

def simulador_biometrico(request):
    return render(request, 'asistencias/simulador_biometrico.html')

def simular_marcaje(request):
    
    ya_marco = Asistencia.objects.filter(fecha_marcaje=timezone.now(), legajo = request.user)
    if not(ya_marco):
        print("No marco")
        asistencia = Asistencia()
        asistencia.fecha_marcaje = timezone.now().date()
        asistencia.hora_entrada = timezone.now().time()
        asistencia.condicion = "Entró"
        asistencia.legajo = request.user
        asistencia.save()
        return redirect('index')
    else:
        marcaje = Asistencia.objects.get(fecha_marcaje=timezone.now(), legajo = request.user)
        if marcaje.hora_salida == None:
            marcaje.hora_salida = timezone.now().time()
            marcaje.condicion = "Asistió"
            marcaje.save()
    return redirect('index')

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

def inasistencia_automatica(request):
    asist_dehoy = Asistencia.objects.filter(fecha_marcaje=datetime.date.today()) 
    print(asist_dehoy)
    users_sinmarcar = CustomUser.objects.exclude(pk__in=asist_dehoy)
    print(users_sinmarcar)

    return redirect('index')
    

