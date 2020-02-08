from django.urls import path

from . import views

urlpatterns = [
    path('audit_tjust', views.audit_tjust, name='audit_tjust'),
    path('audit_tjust_detail/<int:pk>', views.audit_tjust_detail, name='audit_tjust_detail'),
    path('audit_tjust_detail_json/<int:pk>/<int:id_history>', views.audit_tjust_detail_json, name='audit_tjust_detail_json'),
    path('audit_just', views.audit_just, name='audit_just'),
    path('audit_just_detail/<int:pk>', views.audit_just_detail, name='audit_just_detail'),
    path('audit_just_detail_json/<int:pk>/<int:id_history>', views.audit_just_detail_json, name='audit_just_detail_json'),
    path('audit_asist', views.audit_asist, name='audit_asist'),
    path('audit_asist_detail/<int:pk>', views.audit_asist_detail, name='audit_asist_detail'),
    path('audit_asist_detail_json/<int:pk>/<int:id_history>', views.audit_asist_detail_json, name='audit_asist_detail_json'),
    path('audit_horarios', views.audit_horario, name='audit_horario'),
    path('audit_horario_detail/<int:pk>', views.audit_horario_detail, name='audit_horario_detail'),
    path('audit_horario_detail_json/<int:pk>/<int:id_history>', views.audit_horario_detail_json, name='audit_horario_detail_json'),
    path('audit_horarios_fijos', views.audit_horario_fijo, name='audit_horario_fijo'),
    path('audit_horario_fijo_detail/<int:pk>', views.audit_horario_fijo_detail, name='audit_horario_fijo_detail'),
    path('audit_horario_fijo_detail_json/<int:pk>/<int:id_history>', views.audit_horario_fijo_detail_json, name='audit_horario_fijo_detail_json'),
    
]