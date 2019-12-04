from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eliminar_detalle_horario/<int:pk>', views.eliminar_detalle_horario, name='eliminar_detalle_horario'),
    path('editar_declaracion_horarios/<int:pk>', views.editar_declaracion_horarios, name='editar_declaracion_horarios'),
    path('finalizar_declaracion_horarios/<int:pk>', views.finalizar_declaracion_horarios, name='finalizar_declaracion_horarios'),
]