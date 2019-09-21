from django.shortcuts import render
from .services import *
import json

# Create your views here.

def home(request):
    context = get_agentes()
    return render(request, 'sayl/pruebaapi.html', {'agentes':context})

def profile(request):
    agente = get_agente(request.user.legajo)
    context = {'agente':agente}
    return render(request, 'sayl/profile.html', context)