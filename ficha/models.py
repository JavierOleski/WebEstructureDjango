from django.db import models

# Create your models here.

class Ficha_basica(models.Model):
    nombre  = models.CharField(max_length=20)
    dni     = models.DecimalField(decimal_places=0, max_digits=8)
    edad    = models.DecimalField(decimal_places=0, max_digits=8)