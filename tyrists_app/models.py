from django.db import models

# Create your models here.
class Tyrs(models.Model):##Таблица туров
    TyrName = models.CharField(max_length=128)
    TyrType = models.CharField(max_length=1024)
    TyrPrice = models.CharField(max_length=60)
    TyrPhoto = models.CharField(max_length=1024,null=True,blank=True)

    def __str__(self):
        return self.TyrName