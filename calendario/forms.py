from django import forms
from .models import Feriado

class FeriadoForm(forms.ModelForm):
    class Meta:
        model = Feriado
        fields = ['descripcion', 'nro_dia', 'mes']