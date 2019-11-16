from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from mensajeria.forms import TelefonoForm
# from mensajeria.forms import UserContactForm
# from mensajeria.models import UserContact


def signin(request):
    pass

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
