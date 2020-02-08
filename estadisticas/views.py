from django.shortcuts import render
from asistencias.models import Asistencia
from django.db.models import Count
from django.http import JsonResponse

# Create your views here.

def estadistica_estados_marcajes(request):
    labels = []
    data = []
    fecha_rango = request.GET.get('fechona')
    user_pk = request.GET.get('user_pk')
    if fecha_rango != '':
        print(fecha_rango)
        f_desde, f_hasta = fecha_rango.split(' - ')
    else:
        f_desde, f_hasta = ['','']
    print("----------->>>>>>> ", user_pk, ">>", fecha_rango)
    if user_pk == 'all' and fecha_rango == '':
        queryset = Asistencia.objects.values('condicion').order_by('condicion').annotate(count=Count('condicion'))
    elif user_pk == 'all' and fecha_rango != '':
        #formatear fecha:
        
        f_desde = f_desde[-4:] + "-" + f_desde[3:5] + "-" + f_desde[0:2]
        f_hasta = f_hasta[-4:] + "-" + f_hasta[3:5] + "-" + f_hasta[0:2]
        queryset = Asistencia.objects.filter(fecha_marcaje__range=(f_desde, f_hasta)).values('condicion').order_by('condicion').annotate(count=Count('condicion'))
        print(f_desde, " - ", f_hasta)
        print(queryset)
    elif user_pk != 'all' and fecha_rango == '':
        queryset = Asistencia.objects.filter(legajo__pk=user_pk).values('condicion').order_by('condicion').annotate(count=Count('condicion'))
    else:
        queryset = Asistencia.objects.filter(legajo__pk=user_pk, fecha_marcaje__range=(f_desde, f_hasta)).values('condicion').order_by('condicion').annotate(count=Count('condicion'))
    for entry in queryset:
        labels.append(entry['condicion'])
        data.append(entry['count'])

    return JsonResponse(data={
        'labels': labels,
        'data': data
    })