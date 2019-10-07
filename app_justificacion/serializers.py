from rest_framework import serializers
from .models import Justificacion

class JustificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Justificacion
        fields = ['descripcion','tipo_justificacion', 'fecha_inicio', 'fecha_fin']
        