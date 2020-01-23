from django.db import models

# Create your models here.

class Configuraciones(models.Model):
    #Configuracion General

    #Configuracion de Reportes
    nombre_universidad = models.CharField(max_length=200)
    nombre_facultad = models.CharField(max_length=200)
    direccion_facultad = models.CharField(max_length=200)
    

    #Configuracion de Asistencias
    tiempo_tolerancia = models.FloatField()

    #Configuracion de Horarios
    porcentaje_frente_aula = models.FloatField()
    horas_a_cumplir_default = models.FloatField()

    #Configuracion de Usuario
    


