from django import forms
from .models import DetalleHorario, HorariosFijos

class DetalleHorarioForm(forms.ModelForm):
    class Meta:
        model = DetalleHorario
        fields = ['descripcion', 'dia', 'desde', 'hasta']
        widgets = {            
            'desde' : forms.TimeInput(attrs={'type':'text','class' : 'form-control time'}),
            'hasta' : forms.TimeInput(attrs={'type':'text','class' : 'form-control time'}),
        }

class HorariosFijosForm(forms.ModelForm):
    class Meta:
        model = HorariosFijos
        fields = ['hora_entrada', 'horas_a_cumplir']
        widgets = {            
            'hora_entrada' : forms.TimeInput(attrs={'type':'text','class' : 'form-control time'}),
            'horas_a_cumplir' : forms.TimeInput(attrs={'type':'text','class' : 'form-control time'}),
        }