from django.shortcuts import render
from .services import *
import json

# Create your views here.

def home(request):
    context = get_agentes()
    return render(request, 'sayl/pruebaapi.html', {'agentes':context})