from django.shortcuts import render, redirect
from .forms import JustificacionForm
from .models import Justificacion

# Create your views here.

def index(request):
    justificaciones = Justificacion.objects.all()
    return render(request, 'app_justificacion/index_admin.html', {'justificaciones':justificaciones})

def avisar_inasistencia(request):
    form_justificacion = JustificacionForm()
    justificaciones = Justificacion.objects.all()

    if request.method == 'POST':
        form_justificacion = JustificacionForm(request.POST)
        if form_justificacion.is_valid():
            just = form_justificacion.save(commit=False)
            just.legajo =  request.user.legajo            
            just.save()
            return redirect('avisar_inasistencia')
    else:
        form_justificacion = JustificacionForm()
        


    context = {'form_justificacion':form_justificacion, 'justificaciones':justificaciones}
    return render(request, 'app_justificacion/avisar_inasistencia.html',context)
