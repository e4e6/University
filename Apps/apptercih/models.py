from django.db import models

# Create your models here.
class PuanHesaplamaModel(models.Model):


    siralama = models.IntegerField(default=0)
    hamPuan = models.FloatField(default=0)
    yerlestirmePuan = models.FloatField(default=0)