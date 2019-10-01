from django.shortcuts import render
from .forms import JustificacionForm

# Create your views here.

def index(request):
    return render(request, 'app_justificacion/index_admin.html')

def avisar_inasistencia(request):
    form_justificacion = JustificacionForm()


    if request.method == 'POST':
        form_justificacion = JustificacionForm(request.POST)
        if form_justificacion.is_valid():
            form_justificacion.save()
            return redirect('index')
    else:
        form_justificacion = JustificacionForm()


    context = {'form_justificacion':form_justificacion}
    return render(request, 'app_justificacion/avisar_inasistencia.html',context)
