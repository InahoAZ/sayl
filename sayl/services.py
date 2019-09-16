import requests as req

def get_agentes():
    url = "http://mapuche.siu.edu.ar/mapuche/rest/agentes"
    user = 'demo'
    password =  'demo'
    resp = req.get(url, auth=(user,password))
    respuesta = resp.json()
    return respuesta

def get_categorias():
    url = "http://mapuche.siu.edu.ar/mapuche/rest/categorias" 
    user = 'demo'
    password = 'demo'
    resp = req.get(url, auth=(user,password))
    respuesta = resp.json() 
    return respuesta  



