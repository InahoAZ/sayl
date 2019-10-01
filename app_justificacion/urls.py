from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('avisar_inasistencia', views.avisar_inasistencia, name='avisar_inasistencia'),

]