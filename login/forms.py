from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'legajo', 'first_name','last_name', 'email', 'suscripto_mail', 'suscripto_telefono'  ) #Legajo para pruebas, despues tiene que ser automatico

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name','last_name', 'email', 'legajo') #Legajo para pruebas, despues tiene que ser automatico
        #fields = ('username', 'email')