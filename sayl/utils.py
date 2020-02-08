from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime, timedelta, date


def dia_de_semana(num_day):
    DAYS = ['Domingo', 'Lunes', 'Martes','Miercoles', 'Jueves', 'Viernes', 'Sábado']
    return DAYS[num_day]

def dia_de_mes(num_month):
    MONTHS = ['Enero', 'Febrero', 'Marzo','Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    return MONTHS[num_month-1]

def time2timedelta(time):
    return datetime.combine(date.min, time) - datetime.min

def date2timedelta(time):
    return datetime.combine(date.min, datetime) - datetime.min

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def get_next_or_prev(models, item, direction):
    '''
    Returns the next or previous item of
    a query-set for 'item'.

    'models' is a query-set containing all
    items of which 'item' is a part of.

    direction is 'next' or 'prev'

    '''
    getit = False
    if direction == 'prev':
        models = models.reverse()
    for m in models:
        if getit:
            return m
        if item == m:
            getit = True
    if getit:
        # This would happen when the last
        # item made getit True
        return models[0]
    return False

    