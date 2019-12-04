from django.db import models

# Create your models here.

class Configuraciones(models.Model):
    nombre_config = models.CharField(max_length=200)
    valor_config = models.FloatField()
    tipo_dato_config = models.CharField(max_length=200)
    


