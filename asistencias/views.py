from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Asistencia
from django.utils import timezone


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

