from django.db import models

# Create your models here.
class DienVien(models.Model):
    ten_dien_vien = models.CharField(max_length=255)
    nam_sinh = models.DateTimeField(null=True)
    anh = models.CharField()
    mo_ta = models.TextField()

class DaoDien(models.Model):
    ten_dao_dien = models.CharField(max_length=255)
    nam_sinh = models.DateTimeField(null=True)
    anh = models.CharField()
    mo_ta = models.TextField()

