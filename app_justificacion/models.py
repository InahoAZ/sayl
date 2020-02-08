from django.db import models
from app_tipojustificacion.models import TipoJustificacion
from login.models import CustomUser
from simple_history.models import HistoricalRecords

# Create your models here.

class Justificacion(models.Model):
    ESTADOS = [
        ('Pendiente','Pendiente'), 
        ('En Auditoria','En proceso de auditoria'),
        ('Aprobado','Aprobado'),
        ('Rechazado','Rechazado'),
        ('Anulado por Marcaje','Anulado por Marcaje'),
        ]
    legajo = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    tipo_justificacion = models.ForeignKey(TipoJustificacion, on_delete=models.PROTECT) 
    estado = models.CharField(max_length=25, default=ESTADOS[0][0], choices=ESTADOS)
    fecha_solicitud = models.DateField(auto_now=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.CharField(max_length=255)
    observaciones_supervisor = models.CharField(max_length=255)
    history = HistoricalRecords(table_name='justificacion_historial')
    

