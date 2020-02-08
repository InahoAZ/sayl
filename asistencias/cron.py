from asistencias.models import Asistencia

#Tarea para asignar inasistencia a todos aquellos que no marcaron en el dia.
def asignar_inasistencia():
    asist_dehoy = Asistencia.objects.filter(fecha_marcaje=datetime.date.today()) 
    print(asist_dehoy)
    users_sinmarcar = CustomUser.objects.exclude(pk__in=asist_dehoy)
    print(users_sinmarcar)
