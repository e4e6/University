from django.db import models

# Create your models here.


class Lisans42020(models.Model):
   ProgramKodu = models.IntegerField()
   UniversiteAdi = models.TextField()
   FakulteAdi = models.TextField()
   BolumAdi = models.TextField()
   PuanTuru = models.TextField()
   GenelKontenjan = models.IntegerField(null=True, blank=True)
   Yerlesen = models.IntegerField(null=True, blank=True)
   EnKucukPuan = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True)
   EnBuyukPuan = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True)
   OBKontenjan = models.IntegerField(null=True, blank=True)
   OBYerlesen = models.IntegerField(null=True, blank=True)
   OBEnKucukPuan = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True)
   OBEnBuyukPuan = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True)


class OnLisans2020(models.Model):
   ProgramKodu = models.IntegerField()
   UniversiteAdi = models.TextField()
   FakulteAdi = models.TextField()
   BolumAdi = models.TextField()
   PuanTuru = models.TextField()
   GenelKontenjan = models.IntegerField(null=True, blank=True)
   Yerlesen = models.IntegerField(null=True, blank=True)
   EnKucukPuan = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True)
   EnBuyukPuan = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True)
   OBKontenjan = models.IntegerField(null=True, blank=True)
   OBYerlesen = models.IntegerField(null=True, blank=True)
   OBEnKucukPuan = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True)
   OBEnBuyukPuan = models.DecimalField(max_digits=10, decimal_places=4,null=True, blank=True)