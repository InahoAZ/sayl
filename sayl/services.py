import requests as req
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError

def get_agentes():
    url = "http://mapuche.siu.edu.ar/mapuche/rest/agentes"
    user = 'demo'
    password =  'demo'
    try:
        resp = req.get(url, auth=(user,password), timeout=1)
        respuesta = resp.json()
    except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
        respuesta = None            
    
    return respuesta

def get_agente(legajo):
    url = "http://mapuche.siu.edu.ar/mapuche/rest/agentes/" + legajo
    user = 'demo'
    password =  'demo'
    try:
        resp = req.get(url, auth=(user,password),timeout=1)
        respuesta = resp.json()
    except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
        respuesta = None            
    return respuesta

def get_categorias(cod_categ = ''):
    url = "http://mapuche.siu.edu.ar/mapuche/rest/categorias" 
    user = 'demo'
    password = 'demo'
    try:
        resp = req.get(url, auth=(user,password),timeout=1)
        respuesta = resp.json()
    except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
        respuesta = None         
    if cod_categ != '' and respuesta != None:
        for r in respuesta:
            if categoria["categoria"].strip() == cod_categ:
                return r
    #print(respuesta)
    return respuesta

def get_cargos_api(legajo, cod_cargo=None):
    url = "http://mapuche.siu.edu.ar/mapuche/rest/agentes/"+legajo+"/cargos" 
    user = 'demo'
    password = 'demo'
    
    #print(url)
    try:
        resp = req.get(url, auth=(user,password),timeout=1)
        respuesta = resp.json()
        if not(cod_cargo == None):
            for r in respuesta:
                if r['cargo'] == cod_cargo:
                    respuesta = None
                    respuesta = r
    except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
        respuesta = None
    return respuesta







