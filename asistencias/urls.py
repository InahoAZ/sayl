from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simulador_biometrico', views.simulador_biometrico, name='simulador_biometrico'),
    path('simular_marcajeeste', views.simular_marcaje, name='simular_marcajeeste'),
    path('corregir_marcaje/<int:pk>', views.corregir_marcaje, name='corregir_marcaje'),
    path('inasistencia_automatica', views.inasistencia_automatica, name='inasistencia_automatica'),

]