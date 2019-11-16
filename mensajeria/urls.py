from django.urls import path

from . import views

urlpatterns = [
    path('mandar_mail', views.mandar_mail, name='mandar_mail'),
    path('mandar_whatsapp', views.mandar_whatsapp, name='mandar_whatsapp'),

    
]