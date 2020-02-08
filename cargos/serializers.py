from rest_framework import serializers
from .models import CargosCache

class CargosCacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargosCache
        fields = '__all__'