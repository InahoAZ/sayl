from rest_framework import serializers
from .models import Justificacion
from app_tipojustificacion.serializers import TipoJustificacionSerializer
from login.serializers import CustomUserSerializer

class JustificacionSerializer(serializers.ModelSerializer):
    tipo_justificacion = TipoJustificacionSerializer()
    legajo = CustomUserSerializer()
    class Meta:
        model = Justificacion
        fields = ['pk','legajo','descripcion','tipo_justificacion', 'fecha_solicitud','fecha_inicio', 'fecha_fin','estado']
        