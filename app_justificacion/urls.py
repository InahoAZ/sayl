from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('avisar_inasistencia', views.avisar_inasistencia, name='avisar_inasistencia'),
    path('justificaciones_list', views.justificaciones_list, name='justificaciones_list'),

]