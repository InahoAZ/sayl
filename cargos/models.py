from django.db import models

# Create your models here.


class CargosCache(models.Model):
    cargo_cod = models.IntegerField()
    categoria = models.CharField(max_length=200)
    desc_regional = models.CharField(max_length=200)
    desc_categ = models.CharField(max_length=200)
    desc_dedic = models.CharField(max_length=200)
    horas_dedicacion = models.IntegerField()
    escalafon = models.CharField(max_length=200) 
    seleccionado = models.BooleanField(default=False)