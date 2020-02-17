from django.db import models
from login.models import CustomUser
from simple_history.models import HistoricalRecords
from datetime import date, datetime
from edificios.models import Edificio
from django.db.models import Func, F



# Create your models here.

class Asistencia(models.Model):
    CONDICIONES = [
        ('Inasistencia Injustificada','Inasistencia Injustificada'),
        ('Inasistencia Justificada','Inasistencia Justificada'),
        ('Inconsistencia Marcaje','Inconsistencia Marcaje'),
        ('Correccion Inconsistencia', 'Correccion Inconsistencia'),
        ('Anulacion por Marcaje', 'Anulacion por Marcaje'),
        ('Marcaje Válido', 'Marcaje Válido'),
        ('Horas a Favor', 'Horas a Favor'),

        ]
    legajo = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    fecha_marcaje = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField(null=True, blank=True)
    condicion = models.CharField(max_length=50, choices=CONDICIONES)
    history = HistoricalRecords()
    edificio = models.ForeignKey(Edificio, on_delete=models.PROTECT)


    @property
    def horas_trabajadas(self):
        if self.hora_entrada != None and self.hora_salida != None:
            hs_entrada = datetime.combine(date.min, self.hora_entrada) - datetime.min
            hs_salida = datetime.combine(date.min, self.hora_salida) - datetime.min
            horas_trabajadas = hs_salida - hs_entrada
        else:
            horas_trabajadas = "00:00:00"
        return str(horas_trabajadas).split('.')[0] 

class Month(Func):
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.IntegerField()