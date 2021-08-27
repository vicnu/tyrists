from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from PIL import Image
# Create your models here.
class Tyrs(models.Model):##Таблица туров
    TyrName = models.CharField(max_length=128)
    TyrType = models.CharField(max_length=1024)
    TyrPrice = models.CharField(max_length=60)
    TyrPhoto = models.CharField(max_length=1024,null=True,blank=True)

    Author = models.ForeignKey(User, null=True, default=None, blank=True, on_delete=models.CASCADE)
    CreationDate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(default="tyr_default.jpg", null=True, blank=True, upload_to='tyrs_imgs')
    TyrPoint = models.CharField(max_length=1024,null=True,blank=True)
    def __str__(self):
        return self.TyrName

    def get_absolute_url(self):
      return reverse("tyr_detail", kwargs={"pk": self.pk})

    def save(self,*args,**kwargs):
        super().save(*args, **kwargs)
        img=Image.open(self.image.path)

        if img.height>300 or img.width>300:
            img.thumbnail((300,300))
            img.save(self.image.path)
    class Meta:
        ordering = ('-CreationDate',)

