from django.shortcuts import render, redirect
from .models import Feriado
from .forms import FeriadoForm
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    feriados = Feriado.objects.all()

    if request.method == 'POST':
        form = FeriadoForm(request.POST)
        print("error: ", form.errors)
        if form.is_valid():
            form.save()
    else:
        form = FeriadoForm()
    
    context ={'feriados':feriados, 'form_feriado':form}
    return render(request, 'calendario/index.html', context)

def eliminar_feriado(request, pk):
    feriados = get_object_or_404(Feriado, pk=pk)
    feriados.delete()
    return redirect('/calendario/')

