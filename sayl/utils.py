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

    