from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from edificios.models import Edificio, Provincia
from .forms import DetalleHorarioForm
from django.contrib import messages


# Create your views here.

def index(request):
    d_horarios = DetalleHorario.objects.all()
    form_detalle_horario = DetalleHorarioForm()
    if request.method == 'POST': 
        form_detalle_horario = DetalleHorarioForm(request.POST)   
        print("Error: ", form_detalle_horario.errors)    
        if form_detalle_horario.is_valid():            
            h = Horario.objects.filter(legajo=request.user.legajo)
            
            if h.count() > 0:
                print("Existe")
                desde = form_detalle_horario.cleaned_data['desde'] 
                hasta = form_detalle_horario.cleaned_data['hasta']            
                dia = form_detalle_horario.cleaned_data['dia']            
                horario = Horario.objects.get(legajo=request.user.legajo)
                d = DetalleHorario.objects.filter(desde=desde, hasta=hasta, dia=dia)
                if d.count() > 0:
                    messages.error(request, 'Ya existe este horario establecido.')
                else:                    
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
    horario = None
    return render(request, 'app_horarios/index.html', {'horario':horario, 'd_horarios':d_horarios, 'form_detalle_horario':form_detalle_horario})
    


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