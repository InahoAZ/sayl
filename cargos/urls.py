from django.urls import path

from . import views

urlpatterns = [
    path('switch_cargo/<int:cod_cargo>', views.switch_cargo, name='switch_cargo'),
    path('mis_cargos_list/', views.mis_cargos_list, name='mis_cargos_list'),

]