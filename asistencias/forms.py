from django import forms
from .models import Asistencia

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['hora_entrada','hora_salida', 'condicion']
        widgets = {
            'descripcion' : forms.TextInput(attrs={'class' : 'form-control col-md-7 col-xs-12'}),            
            'hora_entrada' : forms.TimeInput(attrs={'type':'time','class' : 'form-control has-feedback-left col-md-7 col-xs-12'}),
            'hora_salida' : forms.TimeInput(attrs={'type':'time','class' : 'form-control has-feedback-left col-md-7 col-xs-12'}),
            'condicion' : forms.Select(attrs={'class' : 'form-control col-md-7 col-xs-12'}),
        }