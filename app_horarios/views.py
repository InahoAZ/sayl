from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from edificios.models import Edificio, Provincia
from .forms import DetalleHorarioForm


# Create your views here.

def index(request):
    horarios = DetalleHorario.objects.all()
    form_detalle_horario = DetalleHorarioForm()
    if request.method == 'POST': 
        form_detalle_horario = DetalleHorarioForm(request.POST)   
        print("Error: ", form_detalle_horario.errors)    
        if form_detalle_horario.is_valid():            
            h = Horario.objects.filter(pk=1)
            
            if h.count() > 0:
                print("Existe")
                horario = Horario.objects.get(legajo=request.user.legajo)
                detalle_horario = form_detalle_horario.save(commit=False)
                detalle_horario.horario = horario
                detalle_horario.save()
            else:
                print("No existe")
                edificio = Edificio.objects.get(pk=1)
                periodo_lectivo = PeriodoLectivo.objects.get(pk=1)

                horario = Horario(edificio=edificio,periodo_lectivo=periodo_lectivo,legajo=request.user.legajo, cant_modificaciones=2) #SETTINGS -> Parametrizar cant_modif
                horario.save()
                print(horario)
                detalle_horario = form_detalle_horario.save(commit=False)
                detalle_horario.horario = horario
                detalle_horario.save()

            

    return render(request, 'app_horarios/index.html', {'horarios':horarios, 'form_detalle_horario':form_detalle_horario})
    
