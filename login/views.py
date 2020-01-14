from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from .models import CustomUser
from sayl.services import get_cargos_api
from cargos.models import CargosCache
from mensajeria.forms import TelefonoForm
# from mensajeria.forms import UserContactForm
# from mensajeria.models import UserContact


def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        #Traigo los cargos de ese usuario del siu
        cargos_siu = get_cargos_api(user.legajo)
        #Selecciono el primero (porque si.)
        cargos_siu = cargos_siu[0]
        #Verifico si no esta en cache
        if not(CargosCache.objects.filter(customuser=user, cargo_cod=cargos_siu['cargo']).exists()):
            #si no esta agrego a cache y selecciono.
            cc = CargosCache(cargo_cod=cargos_siu['cargo'],
                            categoria=cargos_siu['categoria'],
                            desc_regional=cargos_siu['desc_regional'],
                            desc_categ=cargos_siu['desc_categ'],
                            desc_dedic=cargos_siu['desc_dedic'],
                            horas_dedicacion=cargos_siu['cargo'],
                            escalafon=cargos_siu['escalafon'],
                            seleccionado=True)
            cc.save()
            u=CustomUser.objects.get(pk=user.pk)
            u.cargos_cache = cc
            u.save()
        
        return redirect('/')
    else:
        return redirect('accounts/login')
    
        

def signout(request):
    pass

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        telefono_form = TelefonoForm(request.POST)
        if form.is_valid() and telefono_form.is_valid():            
            telid = telefono_form.save()
            formi = form.save(commit=False)            
            print(telid)
            formi.telefono = telid
            formi.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('sayl/index')
    else:
        form = CustomUserCreationForm()
        telefono_form = TelefonoForm(request.POST)
    return render(request, 'login/signup.html', {'form':form,'telefono_form':telefono_form})


# Create your views here.
