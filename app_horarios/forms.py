from django import forms
from .models import DetalleHorario, HorariosFijos

class DetalleHorarioForm(forms.ModelForm):
    class Meta:
        model = DetalleHorario
        fields = ['descripcion', 'dia', 'desde', 'hasta']

class HorariosFijosForm(forms.ModelForm):
    class Meta:
        model = HorariosFijos
        fields = ['hora_entrada', 'horas_a_cumplir']