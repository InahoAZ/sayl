from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eliminar_detalle_horario/<int:pk>', views.eliminar_detalle_horario, name='eliminar_detalle_horario'),
]