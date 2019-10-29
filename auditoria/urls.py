from django.urls import path

from . import views

urlpatterns = [
    path('audit_tjust', views.audit_tjust, name='audit_tjust'),
    path('audit_just', views.audit_just, name='audit_just'),

    
]