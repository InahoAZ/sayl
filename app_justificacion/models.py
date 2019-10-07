from django.db import models
from app_tipojustificacion.models import TipoJustificacion

# Create your models here.

class Justificacion(models.Model):
    ESTADOS = [
        ('Pendiente','Pendiente'), 
        ('En Auditoria','En proceso de auditoria'),
        ('Aprobado','Aprobado'),
        ('Rechazado','Rechazado'),
        ]
    legajo = models.CharField(max_length=12)
    tipo_justificacion = models.ForeignKey(TipoJustificacion, on_delete=models.PROTECT) #CAMBIAR A ONETOMANY
    estado = models.CharField(max_length=16, default=ESTADOS[0][0], choices=ESTADOS)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.CharField(max_length=255)

