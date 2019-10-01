from django.db import models
from app_tipojustificacion.models import TipoJustificacion

# Create your models here.

class Justificacion(models.Model):
    legajo = models.CharField(max_length=12)
    tipo_justificacion = models.ForeignKey(TipoJustificacion, on_delete=models.PROTECT) #CAMBIAR A ONETOMANY
    estado = models.CharField(max_length=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.CharField(max_length=255)

