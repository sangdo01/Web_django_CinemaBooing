from django.db import models
from information.models import Directors, Actor
from datetime import datetime 
from django.template.defaultfilters import slugify
import os

from django.contrib.auth.models import User
# Create your models here.

class Movie(models.Model):
    def image_movie_upload_to(self, instance = None):
        if instance:
            return os.path.join("movie", instance)
        return None

    def image_banner_upload_to(self, instance = None):
        if instance:
            return os.path.join("banner", instance)
        return None
    
    # def getCategories(self):
    #     # list_cate = Movie_Detail.objects.filter(movie_id = self.id)
    #     return  (Movie_Detail.objects.values_list('movie_id').get(movie_id = self.id))

        

    movie_name = models.CharField(max_length= 500)
    content = models.TextField()
    trailer = models.CharField(max_length= 500, null= True)
    image = models.ImageField(default= 'default/no_image.png', upload_to= image_movie_upload_to, max_length= 500)
    banner = models.ImageField(default= 'default/no_image.png', upload_to= image_banner_upload_to, max_length= 500)
    time_of_movie = models.IntegerField(null= True, blank= True)
    language = models.CharField(null= True, blank= True, max_length= 255)
    release_date = models.DateTimeField(null= True)
    # is_showing = 2(cooming soon)
    is_showing = models.IntegerField(default= 2)
    # status = 1(show movie), = 2 (hide movie)
    status = models.IntegerField(default= 2)
    directors = models.ForeignKey(Directors, on_delete= models.CASCADE, null= True, blank=True)
    actors = models.ManyToManyField(Actor, through='Movie_Actor')



    def __str__(self):
        return self.movie_name



class Genre(models.Model):
    genre_name = models.CharField(max_length=255, unique=True)
    movies = models.ManyToManyField(Movie, through='Movie_Genre')


    def __str__(self):
        return self.genre_name


class Movie_Genre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        rs = 'id: '+ str(self.pk) + '\tmovie: ' + str(self.movie) + '\tgenre: ' + str(self.genre)
        return rs


class Movie_Actor(models.Model):
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete = models.CASCADE)

    def __str__(self):
        rs = 'id: '+ str(self.pk) + '\tmovie: ' + str(self.movie) + '\tactor: ' + str(self.actor)
        return rs


class ReviewRating(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=500, blank=True)
    rate = models.IntegerField()
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.moive


# class Movie_Rating(models.Model):
#     rate = models.IntegerField(default=5)
#     content_rate = models.TextField()
#     movie_id = models.ForeignKey(Movie, on_delete= models.CASCADE)
#     khach_hang_id = models.ForeignKey(KhachHang, on_delete= models.CASCADE)


# class RapChieu(models.Model):
#     ten_rap = models.CharField(max_length=255)
#     dia_chi = models.CharField(max_length=255)
#     status = models.IntegerField(default= 1)


# class PhongChieu(models.Model):
#     ten_phong_chieu = models.CharField(max_length=255)
#     so_ghe = models.IntegerField()
#     rap_chieu_id = models.ForeignKey(RapChieu, on_delete= models.CASCADE)
#     status = models.IntegerField(default= 1)


# class LoaiGhe(models.Model):
#     ten_loai_ghe = models.CharField(max_length=255)
#     anh_loai_ghe = models.CharField()
#     phu_thu = models.DecimalField()
#     status = models.IntegerField(default= 1)


# class GheNgoi(models.Model):
#     hang = models.CharField()
#     cot = models.IntegerField()
#     gia_ghe = models.DecimalField()
#     phong_chieu_id = models.ForeignKey(PhongChieu, on_delete= models.CASCADE)
#     loai_ghe_id = models.ForeignKey(LoaiGhe, on_delete= models.CASCADE)
#     status = models.IntegerField(default= 1)


# class SuatChieu(models.Model):
#     ngay_chieu = models.DateTimeField()
#     phim_id = models.ForeignKey(Phim, on_delete= models.CASCADE)
#     phong_chieu_id = models.ForeignKey(PhongChieu, on_delete= models.CASCADE)
#     status = models.IntegerField(default= 1)


# class KhungGio(models.Model):
#     thoi_gian = models.DateTimeField()
#     status = models.IntegerField(default= 1)

 
# class SuatChieu_KhungGio(models.Model):
#     suat_chieu_id = models.ForeignKey(SuatChieu, on_delete= models.CASCADE)
#     khung_gio_id = models.ForeignKey(KhungGio, on_delete= models.CASCADE)

