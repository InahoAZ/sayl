from django import forms
from .models import Configuraciones

class ConfiguracionesForm(forms.ModelForm):
    class Meta:
        model = Configuraciones
        fields = '__all__'
        widgets = {           
            'nombre_config' : forms.TextInput(attrs={'class' : 'form-control has-feedback-left col-md-7 col-xs-12'}),
            'valor_config' : forms.NumberInput(attrs={'class' : 'form-control has-feedback-left col-md-7 col-xs-12'}),
            'tipo_dato_config' : forms.TextInput(attrs={'class' : 'form-control has-feedback-left col-md-7 col-xs-12'}),
        }