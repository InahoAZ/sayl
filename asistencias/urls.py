from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simulador_biometrico', views.simulador_biometrico, name='simulador_biometrico'),
    path('simular_marcaje', views.simular_marcaje, name='simular_marcaje'),

]