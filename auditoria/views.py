from django.shortcuts import render, redirect
from app_tipojustificacion.views import TipoJustificacion


def audit_tjust(request):
    audit_tjusts = TipoJustificacion.history.all()
    context = {'audit_tjusts': audit_tjusts}
    return render(request, 'auditoria/audit_tjust.html', context)
# Create your views here.
