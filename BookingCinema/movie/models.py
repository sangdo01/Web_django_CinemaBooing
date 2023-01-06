from django.db import models
from information.models import DaoDien, DienVien
from datetime import datetime 
# Create your models here.
class Phim(models.Model):
    ten_phim = models.CharField(max_length=500)
    noi_dung = models.TextField()
    trailer = models.CharField()
    anh = models.CharField()
    banner = models.CharField()
    thoi_luong = models.IntegerField(default=0)
    ngay_cong_chieu = models.DateTimeField()
    comingsoon = models.IntegerField()
    status = models.IntegerField(default= 1)



class TheLoaiPhim(models.Model):
    ten_the_loai = models.CharField(max_length=255)


class CT_TheLoaiPhim(models.Model):
    phim_id = models.ForeignKey(Phim, on_delete=models.CASCADE)
    the_loai_phim_id = models.ForeignKey(TheLoaiPhim, on_delete=models.CASCADE)

class CT_DienVien(models.Model):
    phim_id = models.ForeignKey(Phim, on_delete = models.CASCADE)
    dien_vien_id = models.ForeignKey(DienVien, on_delete = models.CASCADE)

# class BinhLuan(models.Model):
#     rate = models.IntegerField(null=True)
#     noi_dung = models.TextField()
#     phim_id = models.ForeignKey(Phim, on_delete= models.CASCADE)
#     khach_hang_id = models.ForeignKey(KhachHang, on_delete= models.CASCADE)

class RapChieu(models.Model):
    ten_rap = models.CharField(max_length=255)
    dia_chi = models.CharField(max_length=255)
    status = models.IntegerField(default= 1)

class PhongChieu(models.Model):
    ten_phong_chieu = models.CharField(max_length=255)
    so_ghe = models.IntegerField()
    rap_chieu_id = models.ForeignKey(RapChieu, on_delete= models.CASCADE)
    status = models.IntegerField(default= 1)


class LoaiGhe(models.Model):
    ten_loai_ghe = models.CharField(max_length=255)
    anh_loai_ghe = models.CharField()
    phu_thu = models.DecimalField()
    status = models.IntegerField(default= 1)

class GheNgoi(models.Model):
    hang = models.CharField()
    cot = models.IntegerField()
    gia_ghe = models.DecimalField()
    phong_chieu_id = models.ForeignKey(PhongChieu, on_delete= models.CASCADE)
    loai_ghe_id = models.ForeignKey(LoaiGhe, on_delete= models.CASCADE)
    status = models.IntegerField(default= 1)

class SuatChieu(models.Model):
    ngay_chieu = models.DateTimeField()
    phim_id = models.ForeignKey(Phim, on_delete= models.CASCADE)
    phong_chieu_id = models.ForeignKey(PhongChieu, on_delete= models.CASCADE)
    status = models.IntegerField(default= 1)

class KhungGio(models.Model):
    thoi_gian = models.DateTimeField()
    status = models.IntegerField(default= 1)
    
class SuatChieu_KhungGio(models.Model):
    suat_chieu_id = models.ForeignKey(SuatChieu, on_delete= models.CASCADE)
    khung_gio_id = models.ForeignKey(KhungGio, on_delete= models.CASCADE)

