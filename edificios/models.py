from django.db import models

# Create your models here.

class Provincia(models.Model):
    descripcion = models.CharField(max_length=200)
    codigo_postal = models.CharField(max_length=30)

class Edificio(models.Model):
    descripcion = models.CharField(max_length=200)
    provincia = models.ForeignKey("Provincia", on_delete=models.PROTECT)