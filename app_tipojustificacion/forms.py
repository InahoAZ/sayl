from django import forms
from .models import TipoJustificacion

class TipoJustificacionForm(forms.ModelForm):
    class Meta:
        model = TipoJustificacion
        fields = ['motivo', 'cargo', 'artcct', 'dia_trabajado','cant_mes', 'cant_año', 'claustro']