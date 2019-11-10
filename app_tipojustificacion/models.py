from django.db import models
from sayl.services import *
from simple_history.models import HistoricalRecords


# Create your models here.

class TipoJustificacion(models.Model):
    CLAUSTRO = [
        ('Docente','Docente'), 
        ('No Docente','No Docente')
        ]
    
    LISTA_CARGOS = []
    categorias = get_categorias()
    if categorias != None:
        for categoria in categorias:        
            t = (categoria.get('categoria'), categoria.get('desc_categ'))
            LISTA_CARGOS.append(t)
    
    motivo = models.CharField(max_length=200)
    artcct = models.CharField(max_length=200)    
    dia_trabajado = models.BooleanField()
    cant_mes = models.IntegerField()
    cant_año = models.IntegerField()
    claustro = models.CharField(
        max_length=11,
        choices=CLAUSTRO)
    cargo  = models.CharField(max_length=20, choices=LISTA_CARGOS, blank=True)
    history = HistoricalRecords(table_name='tjustificacion_historial')

    def __str__(self):
        return self.motivo




'''
class Cargo(models.Model):
    descripcion = models.CharField(max_length=200)
    requisitos = models.CharField(max_length=200)
    horas = models.IntegerField()
    tipo_justificacion = models.ManyToManyField('TipoJustificacion')

    def __str__(self):
        return self.descripcion
'''
