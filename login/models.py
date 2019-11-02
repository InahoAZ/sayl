from django.db import models
from django.contrib.auth.models import AbstractUser
from sayl.services import get_cargos_api
# Create your models here.

class CustomUser(AbstractUser):
    legajo = models.CharField(max_length=12)
    image_profile = models.ImageField(upload_to='images/')
    
    
    def get_cargos(self):
        cargos = get_cargos_api(self.legajo)
        return cargos
    
    # def __str__(self):
    #     return self.get_cargos()