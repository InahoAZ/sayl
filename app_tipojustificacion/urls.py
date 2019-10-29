from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listado_tjust/',views.listado_tjust,name='listado_tjust'),
    path('detalle_tjust/<int:tipo_justificacion_id>/',views.detalle_tjust,name='detalle_tjust'),
    path('agregar_tjust/',views.agregar_tjust,name='agregar_tjust'),
    path('eliminar_tjust/<int:tipo_justificacion_id>/',views.eliminar_tjust,name='eliminar_tjust'),
    path('modificar_tjust/<int:tipo_justificacion_id>/',views.modificar_tjust,name='modificar_tjust'),
    path('tipos_justificacion_list/', views.tipos_justificacion_list, name='tipos_justificacion_list'),
    

    
]