from django.db import models
from login.models import CustomUser
from simple_history.models import HistoricalRecords
from datetime import date, datetime


# Create your models here.

class Asistencia(models.Model):
    legajo = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    fecha_marcaje = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField(null=True, blank=True)
    condicion = models.CharField(max_length=50)
    history = HistoricalRecords()

    @property
    def horas_trabajadas(self):
        if self.hora_entrada != None and self.hora_salida != None:
            hs_entrada = datetime.combine(date.min, self.hora_entrada) - datetime.min
            hs_salida = datetime.combine(date.min, self.hora_salida) - datetime.min
            horas_trabajadas = hs_salida - hs_entrada
        else:
            horas_trabajadas = "-"
        return horas_trabajadas
