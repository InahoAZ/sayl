from django.db import models
#from login.models import CustomUser

# Create your models here.


class CargosCache(models.Model):
    cargo_cod = models.IntegerField()
    categoria = models.CharField(max_length=200)
    desc_regional = models.CharField(max_length=200)
    desc_categ = models.CharField(max_length=200)
    desc_dedic = models.CharField(max_length=200)
    horas_dedicacion = models.FloatField()
    escalafon = models.CharField(max_length=200) 
    seleccionado = models.BooleanField(default=False)
    #agente = models.ManyToManyField(CustomUser)