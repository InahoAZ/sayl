from django.shortcuts import render, redirect
from .forms import ConfiguracionesForm
from .models import Configuraciones

# Create your views here.

def index(request):
    all_config = Configuraciones.objects.order_by('-id')[0]
    config_form = ConfiguracionesForm(instance=all_config)
    if request.method == 'POST':
        form = ConfiguracionesForm(request.POST)
        print(form.errors)
        if form.is_valid():
            config = form.save(commit=False)
            config.changeReason = 'Nueva Configuracion'
            config.save()
            return redirect('/config')
    return render(request, 'config/index.html', {'all_config':all_config, 'config_form':config_form})

def editar_config(request,pk):
    config = Configuraciones.objects.get(pk=pk)
    if request.method == 'GET':
        form = ConfiguracionesForm(instance = config)
    else:
        form = ConfiguracionesForm(request.POST, instance = config)
        print(form.errors)
        if form.is_valid():
            cargos = None
            config = form.save(commit=False)
            config.changeReason = 'Modificacion de Configuracion'
            config.save()
        return redirect('/config')
    
    return render(request, 'config/editar_config.html', {'form':form})