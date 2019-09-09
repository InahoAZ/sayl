from django.db import models

# Create your models here.

class TipoJustificacion(models.Model):
    motivo = models.CharField(max_length=200)
    artcct = models.CharField(max_length=200)
    se_lista = models.BooleanField()
    dia_trabajado = models.BooleanField()
    cant_mes = models.IntegerField()
    cant_año = models.IntegerField()
    claustro = models.CharField(max_length=1)
    borrado = models.BooleanField()

    def __str__(self):
        return self.motivo


class Cargo(models.Model):
    descripcion = models.CharField(max_length=200)
    requisitos = models.CharField(max_length=200)
    horas = models.IntegerField()
    tipo_justificacion = models.ManyToManyField('TipoJustificacion')

    def __str__(self):
        return self.descripcion
