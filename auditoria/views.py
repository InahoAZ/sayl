from django.shortcuts import render, redirect
from app_tipojustificacion.views import TipoJustificacion
from app_justificacion.views import Justificacion


def audit_tjust(request):
    audit_tjusts = TipoJustificacion.history.all()
    context = {'audit_tjusts': audit_tjusts}
    return render(request, 'auditoria/audit_tjust.html', context)

def audit_just(request):
    audit_justs = Justificacion.history.all()
    context = {'audit_justs': audit_justs}
    return render(request, 'auditoria/audit_just.html', context)
