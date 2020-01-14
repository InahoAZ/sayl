from django import forms
from .models import Configuraciones

class ConfiguracionesForm(forms.ModelForm):
    class Meta:
        model = Configuraciones
        fields = '__all__'
        widgets = {           
            
        }