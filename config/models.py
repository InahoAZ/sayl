from django.db import models

# Create your models here.

class Configuraciones(models.Model):
    #Configuracion General

    #Configuracion de Horarios
    nombre_universidad = models.CharField(max_length=200)
    nombre_facultad = models.CharField(max_length=200)
    direccion_facultad = models.CharField(max_length=200)
    

    #Configuracion de Asistencias
    tiempo_tolerancia = models.FloatField()

    #Configuracion de Horarios
    porcentaje_frente_aula = models.FloatField()
    horario_entrada_nodoc = models.TimeField()

    #Configuracion de Usuario
    


