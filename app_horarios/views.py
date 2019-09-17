from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import HorarioForm


# Create your views here.

def index(request):
    horarios = Horario.objects.all()
    form_horarios = HorarioForm()
    if request.method == 'POST':        
        agregar_tjust(request)
    return render(request, 'app_horarios/index.html', {'horarios':horarios, 'form_horarios':form_horarios})
    
