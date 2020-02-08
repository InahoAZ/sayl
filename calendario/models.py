from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

class Feriado(models.Model):
    
    MESES = [
        ('Enero','Enero'),
        ('Febrero', 'Febrero'),
        ('Marzo', 'Marzo'),
        ('Abril', 'Abril'),
        ('Mayo', 'Mayo'),
        ('Junio', 'Junio'),
        ('Julio', 'Julio'),
        ('Agosto', 'Agosto'),
        ('Septiembre', 'Septiembre'),
        ('Octubre', 'Octubre'),
        ('Noviembre', 'Noviembre'),
        ('Diciembre', 'Diciembre')
    ]

    descripcion = models.CharField(max_length=200)
    nro_dia = models.IntegerField()
    mes = models.CharField(max_length=200, choices=MESES)
    history = HistoricalRecords()
