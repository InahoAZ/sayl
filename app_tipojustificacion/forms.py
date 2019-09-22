from django import forms
from .models import TipoJustificacion

class TipoJustificacionForm(forms.ModelForm):
    class Meta:
        model = TipoJustificacion
        fields = ['motivo', 'cargo', 'artcct', 'dia_trabajado','cant_mes', 'cant_año', 'claustro']
        widgets = {
            'motivo' : forms.TextInput(attrs={'class' : 'form-control col-md-7 col-xs-12'}),
            'cargo' : forms.Select(attrs={'class' : 'form-control col-md-7 col-xs-12'}),
            'artcct' : forms.TextInput(attrs={'class' : 'form-control col-md-7 col-xs-12'}),
            'dia_trabajado' : forms.CheckboxInput(attrs={'class' : 'flat'}),
            'cant_mes' : forms.NumberInput(attrs={'class' : 'form-control col-md-7 col-xs-12'}),          
            'cant_año' : forms.NumberInput(attrs={'class' : 'form-control col-md-7 col-xs-12'}),
            'claustro' : forms.Select(attrs={'class' : 'form-control col-md-7 col-xs-12'}),          
        }