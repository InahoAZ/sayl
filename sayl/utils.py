from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import datetime, timedelta, date


from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def dia_de_semana(num_day):
    DAYS = ['Domingo', 'Lunes', 'Martes','Miercoles', 'Jueves', 'Viernes', 'Sábado']
    return DAYS[num_day]

def time2timedelta(time):
    return datetime.combine(date.min, time) - datetime.min

def date2timedelta(time):
    return datetime.combine(date.min, datetime) - datetime.min