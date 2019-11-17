from django.db import models
from edificios.models import Edificio

# Create your models here.
class PeriodoLectivo(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    actual = models.BooleanField()
    descripcion = models.CharField(max_length=200)


class Horario(models.Model):    
    #EDIFICIO DEBERIA IR EN CADA DETALLE DE HORARIO, MODIFICAR.
    edificio = models.ForeignKey(Edificio, on_delete = models.PROTECT, blank=True)    
    periodo_lectivo = models.ForeignKey('PeriodoLectivo', on_delete = models.PROTECT, blank=True)
    legajo = models.CharField(max_length=12)    
    cant_modificaciones = models.IntegerField()
    #activo = models.BooleanField(default=False) #Añadir.
    


class DetalleHorario(models.Model):
    horario = models.ForeignKey('Horario', on_delete = models.PROTECT)
    
    DIAS = [
        ('Lunes', 'Lunes'),
        ('Martes','Martes'),
        ('Miercoles', 'Miercoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sabado', 'Sabado'),
        ('Domingo','Domingo')
    ]
    desde = models.TimeField()
    hasta = models.TimeField()
    dia = models.CharField(
        max_length=10,
        choices = DIAS
    )
    descripcion = models.CharField(max_length=200)
    
    
