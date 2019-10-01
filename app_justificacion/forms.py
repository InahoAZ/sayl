from django import forms
from .models import Justificacion

class JustificacionForm(forms.ModelForm):
    class Meta:
        model = Justificacion
        fields = ['descripcion','tipo_justificacion', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'descripcion' : forms.TextInput(attrs={'class' : 'form-control col-md-7 col-xs-12'}),
            'tipo_justificacion' : forms.Select(attrs={'class' : 'form-control col-md-7 col-xs-12'}),
            'fecha_inicio' : forms.TextInput(attrs={'class' : 'form-control col-md-7 col-xs-12'}),
            'fecha_fin' : forms.TextInput(attrs={'class' : 'form-control col-md-7 col-xs-12'}),
            'cant_mes' : forms.NumberInput(attrs={'class' : 'form-control col-md-7 col-xs-12'}),          
            'cant_año' : forms.NumberInput(attrs={'class' : 'form-control col-md-7 col-xs-12'}),
            'claustro' : forms.Select(attrs={'class' : 'form-control col-md-7 col-xs-12'}),          
        }