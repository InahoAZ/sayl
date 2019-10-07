import requests as req
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError

def get_agentes():
    url = "http://mapuche.siu.edu.ar/mapuche/rest/agentes"
    user = 'demo'
    password =  'demo'
    try:
        resp = req.get(url, auth=(user,password), timeout=0.0001)
        respuesta = resp.json()
    except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
        respuesta = None            
    
    return respuesta

def get_agente(legajo):
    url = "http://mapuche.siu.edu.ar/mapuche/rest/agentes/" + legajo
    user = 'demo'
    password =  'demo'
    try:
        resp = req.get(url, auth=(user,password),timeout=0.0001)
        respuesta = resp.json()
    except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
        respuesta = None            
    return respuesta

def get_categorias(cod_categ = ''):
    url = "http://mapuche.siu.edu.ar/mapuche/rest/categorias" 
    user = 'demo'
    password = 'demo'
    try:
        resp = req.get(url, auth=(user,password),timeout=0.0001)
        respuesta = resp.json()
    except (ConnectTimeout, HTTPError, ReadTimeout, Timeout, ConnectionError):
        respuesta = None         
    if cod_categ != '' and respuesta != None:
        for r in respuesta:
            if categoria["categoria"].strip() == cod_categ:
                return r

    return respuesta




