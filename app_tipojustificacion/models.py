from django.db import models
from sayl.services import *

# Create your models here.

class TipoJustificacion(models.Model):
    CLAUSTRO = [
        ('Docente','Docente'), 
        ('No Docente','No Docente')
        ]
    
    LISTA_CARGOS = []
    '''categorias = get_categorias()
    for categoria in categorias:        
        t = (categoria.get('categoria'), categoria.get('desc_categ'))
        LISTA_CARGOS.append(t)'''
    motivo = models.CharField(max_length=200)
    artcct = models.CharField(max_length=200)    
    dia_trabajado = models.BooleanField()
    cant_mes = models.IntegerField()
    cant_año = models.IntegerField()
    claustro = models.CharField(
        max_length=11,
        choices=CLAUSTRO)
    cargo  = models.CharField(max_length=20, choices=LISTA_CARGOS)  

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
