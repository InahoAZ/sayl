from django.contrib import admin
from .models import Justificacion,TipoJustificacion
from simple_history.admin import SimpleHistoryAdmin
# Register your models here.

admin.site.register(Justificacion, SimpleHistoryAdmin)
