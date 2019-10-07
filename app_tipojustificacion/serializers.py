from rest_framework import serializers
from .models import TipoJustificacion

class TipoJustificacionSerializer(serializers.ModelSerializer):    
    class Meta:
        model = TipoJustificacion
        fields = '__all__'
        