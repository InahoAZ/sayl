from django.shortcuts import render
from .services import *
import json
from config.models import Configuraciones


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        agente = get_agente(request.user.legajo)
        config = Configuraciones.objects.last()
        context = {'agente':agente, 'config':config}    
        return render(request, 'sayl/index.html', context)
    return render(request, 'sayl/index.html')

def profile(request):
    agente = get_agente(request.user.legajo)
    context = {'agente':agente}
    return render(request, 'sayl/profile.html', context)

def edit_contact(request, pk):
    # user_contact = UserContact.objects.get(pk=pk)
    # if request.method == 'GET':
    #     form = UserContactForm(instance = user_contact)
    # else:
    #     form = UserContactForm(request.POST, instance = user_contact)
    #     print(form.errors)
    #     if form.is_valid():
    #         user_contact = form.save(commit=False)
    #         user_contact.changeReason = 'Modificacion de Contacto'
    #         user_contact.save()
    #     return redirect('index')    
    pass
    #return render(request, 'sayl/editar_contacto.html', {'form':form, 'cargos':cargos})

