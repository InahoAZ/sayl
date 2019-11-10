from django import forms
from .models import Justificacion

class JustificacionForm(forms.ModelForm):
    class Meta:
        model = Justificacion
        fields = ['descripcion','tipo_justificacion', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'descripcion' : forms.TextInput(attrs={'class' : 'form-control col-md-7 col-xs-12'}),
            'tipo_justificacion' : forms.Select(attrs={'class' : 'form-control col-md-7 col-xs-12', 'id':'select-just'}),
            'fecha_inicio' : forms.DateInput(format=('%d-%m-%Y'), attrs={'type':'text','class' : 'form-control has-feedback-left col-md-7 col-xs-12','id':'single_cal4','aria-describedby':'inputSuccess2Status2'}),
            'fecha_fin' : forms.DateInput(format=('%d-%m-%Y'),attrs={'type':'text','class' : 'form-control has-feedback-left col-md-7 col-xs-12','id':'single_cal3','aria-describedby':'inputSuccess2Status3'}),
            
        }