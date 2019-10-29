from rest_framework import serializers
from .models import TipoJustificacion

class TipoJustificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoJustificacion
        fields = ['pk','motivo','artcct', 'dia_trabajado', 'cant_mes', 'cant_año', 'claustro','cargo']
