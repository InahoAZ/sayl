from django.shortcuts import render,redirect, HttpResponse
from .models import CargosCache
from login.models import CustomUser
from sayl.services import get_cargos_api
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# from .serializers import JustificacionSerializer
from .serializers import CargosCacheSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

# Create your views here.

def switch_cargo(request, cod_cargo):
    
    #TENGO QUE VER SI HAY ALGUNO SELECCIONADO
    if CargosCache.objects.filter(seleccionado=True).exists():
        cs = CargosCache.objects.filter(seleccionado=True)
        cs.update(seleccionado=False)

    if not(CargosCache.objects.filter(customuser=request.user, cargo_cod=cod_cargo).exists()):       
        
        #Traigo los cargos de ese usuario del siu
        cargo_siu = get_cargos_api(request.user.legajo, cod_cargo)
        #si no esta agrego a cache y selecciono.
        cc = CargosCache(cargo_cod=cargo_siu['cargo'],
                        categoria=cargo_siu['categoria'],
                        desc_regional=cargo_siu['desc_regional'],
                        desc_categ=cargo_siu['desc_categ'],
                        desc_dedic=cargo_siu['desc_dedic'],
                        horas_dedicacion=cargo_siu['cargo'],
                        escalafon=cargo_siu['escalafon'],
                        seleccionado=True)
        cc.save()
        u=CustomUser.objects.get(pk=request.user.pk)
        u.cargos_cache = cc
        u.save()
    else:
        cc = CargosCache.objects.get(customuser=request.user, cargo_cod=cod_cargo)
        if cc.seleccionado == False:
            cc.seleccionado = True
            cc.save()
    return redirect(request.META['HTTP_REFERER'])    

@csrf_exempt
def mis_cargos_list(request):
    
    if request.method == 'GET':
        mis_cargos = get_cargos_api(request.user.legajo)
        serializer = mis_cargos

        # result = dict()
        # result = serializer.data
        return JSONResponse(mis_cargos)

