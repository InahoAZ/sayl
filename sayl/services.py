import requests as req

def get_agentes():
    url = "http://mapuche.siu.edu.ar/mapuche/rest/agentes"
    user = 'demo'
    password =  'demo'
    resp = req.get(url, auth=(user,password))
    respuesta = resp.json()
    return respuesta

def get_categorias(cod_categ = ''):
    url = "http://mapuche.siu.edu.ar/mapuche/rest/categorias" 
    user = 'demo'
    password = 'demo'
    resp = req.get(url, auth=(user,password))
    respuesta = resp.json() 
    if cod_categ != '':
        for r in respuesta:
            if categoria["categoria"].strip() == cod_categ:
                return r

    return respuesta




