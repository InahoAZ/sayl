from django.db import models

from simple_history.models import HistoricalRecords

# Create your models here.

class Telefono(models.Model):
    prefijo = models.CharField(max_length=10)
    caracteristica = models.CharField(max_length=12)
    numero = models.CharField(max_length=35)
    history = HistoricalRecords(table_name='telefono_historial')

    
    
    

