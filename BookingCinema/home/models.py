from django.db import models

# Create your models here.


class Contact(models.Model):
    name= models.CharField(max_length=255)
    email= models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

# class TinTuc(models.Model):
#     tieu_de = models.CharField(max_length=500)
#     anh = models.CharField()
#     noi_dung = models.TextField()
#     status = models.IntegerField(default= 1)
