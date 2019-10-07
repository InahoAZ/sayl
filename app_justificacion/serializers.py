from rest_framework import serializers
from .models import Justificacion
from login.serializers import CustomUserSerializer
from app_tipojustificacion.serializers import TipoJustificacionSerializer

class JustificacionSerializer(serializers.ModelSerializer):
    legajo = CustomUserSerializer()
    tipo_justificacion = TipoJustificacionSerializer()
    class Meta:
        model = Justificacion
        fields = '__all__'
        