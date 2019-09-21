from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signin(request):
    pass

def signout(request):
    pass

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('sayl/index')
    else:
        form = UserCreationForm()
    return render(request, 'login/signup.html', {'form':form})


# Create your views here.
