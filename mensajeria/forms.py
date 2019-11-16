from django import forms
from .models import Telefono
# from mensajeria.models import UserContact

# class UserContactForm(forms.ModelForm):
#     class Meta:
#         model = UserContact
#         fields = ['telefono', 'email', 'suscripto_telefono', 'suscripto_mail']
#         widgets = {
#             'motivo' : forms.TextInput(attrs={'class' : 'form-control col-md-7 col-xs-12'}),
#         }
class TelefonoForm(forms.ModelForm):
    class Meta:
        model = Telefono
        fields = ['prefijo', 'caracteristica', 'numero']
