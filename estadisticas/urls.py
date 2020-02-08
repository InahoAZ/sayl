from django.urls import path
from . import views

urlpatterns = [
    path('estadistica_estados_marcajes/', views.estadistica_estados_marcajes, name='estadistica_estados_marcajes'),
    path('estadistica_estados_marcajes/<int:agente_pk>', views.estadistica_estados_marcajes, name='estadistica_estados_marcajes'),
    

]