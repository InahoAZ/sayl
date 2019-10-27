from django.urls import path

from . import views

urlpatterns = [
    path('audit_tjust', views.audit_tjust, name='audit_tjust'),

    
]