from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('avisar_inasistencia', views.avisar_inasistencia, name='avisar_inasistencia'),
    path('justificaciones_list/<int:pk>', views.justificaciones_list, name='justificaciones_list'),
    path('aprobar_just/<int:pk>', views.aprobar_just, name='aprobar_just'),
    path('rechazar_just/<int:pk>', views.rechazar_just, name='rechazar_just'),
    path('cancelar_aviso/<int:pk>', views.cancelar_aviso, name='cancelar_aviso'),
    path('justificaciones_encurso', views.justificaciones_encurso, name='justificaciones_encurso'),

]