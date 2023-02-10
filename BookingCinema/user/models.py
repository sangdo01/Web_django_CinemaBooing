from django.db import models


# Create your models here.

class Member(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=10, null= True)
    password = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add= True, null= True)



