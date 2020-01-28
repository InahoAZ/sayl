from django.db import models
from django.contrib.auth.models import AbstractUser
from sayl.services import get_cargos_api
from mensajeria.models import Telefono
from simple_history.models import HistoricalRecords
from cargos.models import CargosCache

# Create your models here.

class CustomUser(AbstractUser):
    legajo = models.CharField(max_length=12)
    image_profile = models.ImageField(upload_to='images/', blank=True)
    telefono = models.ForeignKey(Telefono, on_delete=models.PROTECT)    
    suscripto_telefono =  models.BooleanField(default=True)
    suscripto_mail = models.BooleanField(default=True)
    cargos_cache = models.ManyToManyField(CargosCache)

    history = HistoricalRecords(table_name='usercontact_historial')
    
    
    def get_cargos(self):
        cargos = get_cargos_api(self.legajo)
        return cargos

    @property
    def cargo_seleccionado(self):
        c_select = CargosCache.objects.get(seleccionado=True, customuser=self)
        return c_select

    def __str__(self):
        return self.last_name + " " + self.first_name + " (" + self.legajo + ")"