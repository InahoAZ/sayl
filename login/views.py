from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


def signin(request):
    pass

def signout(request):
    pass

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("Hola")
            print(form)
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('sayl/index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'login/signup.html', {'form':form})


# Create your views here.
