from django.db import models

# Create your models here.











class LienHe(models.Model):
    ho_ten = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    tieu_de = models.CharField(max_length=255)
    noi_dung = models.TextField()
    status = models.IntegerField(default= 1)

class TinTuc(models.Model):
    tieu_de = models.CharField(max_length=500)
    anh = models.CharField()
    noi_dung = models.TextField()
    status = models.IntegerField(default= 1)
