from django import forms
from .models import DetalleHorario

class DetalleHorarioForm(forms.ModelForm):
    class Meta:
        model = DetalleHorario
        fields = ['descripcion', 'dia', 'desde', 'hasta']