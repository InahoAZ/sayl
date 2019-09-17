from django.db import models

# Create your models here.
class PeriodoLectivo(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    actual = models.BooleanField()
    descripcion = models.CharField(max_length=200)

class Modulo(models.Model):
    descripcion = models.CharField(max_length=200)


class Horario(models.Model):
    DIAS = [
        ('Lunes', 'Lunes'),
        ('Martes','Martes'),
        ('Miercoles', 'Miercoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sabado', 'Sabado'),
        ('Domingo','Domingo')
    ]
    modulo = models.ForeignKey('Modulo', on_delete = models.PROTECT)
    periodo_lectivo = models.ForeignKey('PeriodoLectivo', on_delete = models.PROTECT)
    legajo = models.CharField(max_length=12)
    desde = models.TimeField()
    hasta = models.TimeField()
    dia = models.CharField(
        max_length=10,
        choices = DIAS
    )
    cant_modificaciones = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    
    
