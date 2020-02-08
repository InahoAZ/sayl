"""sayl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings    
from django.urls import path, include
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home' ),
    path('perfil/', views.profile, name='perfil' ),
    path('edit_contact/<int:pk>', views.edit_contact, name='edit_contact'),
    path('app_tipojustificacion/', include('app_tipojustificacion.urls')),
    path('app_horarios/', include('app_horarios.urls')),
    path('app_justificacion/', include('app_justificacion.urls')),
    path('login/', include('login.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('auditoria/', include('auditoria.urls')),
    path('asistencias/', include('asistencias.urls')),
    path('edificios/', include('edificios.urls')),
    path('mensajeria/', include('mensajeria.urls')),
    path('config/', include('config.urls')),
    path('cargos/', include('cargos.urls')),
    path('calendario/', include('calendario.urls')),
    path('estadisticas/', include('estadisticas.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)












if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns



