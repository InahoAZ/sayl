from django.shortcuts import render
from .services import *
import json

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        agente = get_agente(request.user.legajo)
        context = {'agente':agente}    
        return render(request, 'sayl/pruebaapi.html', {'agente':agente})
    return render(request, 'sayl/pruebaapi.html')

def profile(request):
    agente = get_agente(request.user.legajo)
    context = {'agente':agente}
    return render(request, 'sayl/profile.html', context)