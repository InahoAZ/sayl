from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editar_config/<int:pk>', views.editar_config, name='editar_config'),
    

]