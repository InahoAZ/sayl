from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eliminar_feriado/<int:pk>', views.eliminar_feriado, name='eliminar_feriado'),
    

]