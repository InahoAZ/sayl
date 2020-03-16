from django import forms
from .models import Asistencia

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['hora_entrada','hora_salida', 'condicion']
        widgets = {
            'descripcion' : forms.TextInput(attrs={'class' : 'form-control col-md-2 col-xs-12'}),            
            'hora_entrada' : forms.TimeInput(attrs={'type':'text','class' : 'form-control time'}),
            'hora_salida' : forms.TimeInput(attrs={'type':'text','class' : 'form-control time'}),
            'condicion' : forms.Select(attrs={'class' : 'select2 form-control col-md-2 col-xs-12'}),
        }