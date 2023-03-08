from django.db import models

# custom User
from django.contrib.auth. models import AbstractBaseUser, BaseUserManager

from django.contrib.auth.models import AbstractUser
# Create your models here.

# class Member(models.Model):
#     username        = models.CharField(max_length=20)
#     email           = models.EmailField(max_length=50)
#     phone_number    = models.CharField(max_length=10, null= True)
#     password        = models.CharField(max_length=20)
#     create_at       = models.DateTimeField(auto_now_add= True, null= True)



# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, first_name, last_name, password = None):
#         if not email:
#             raise ValueError("Phai la email")
#         if not username:
#             raise ValueError("Phai co username")
#         if not first_name:
#             raise ValueError("Phai co first name")
#         if not last_name:
#             raise ValueError("Phai co last name")

#         user = self.model(
#             email = self.normalize_email(email),
#             username = username,
#         )

#         user.set_password(password)
#         user.save(using = self._db)
#         return user

#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email = self.normalize_email(email),
#             password = password,
#             username = username,
#         )

#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using = self._db)
#         return user


# class Account(AbstractBaseUser):
#     email           = models.EmailField(verbose_name= 'email', max_length= 60, unique= True)
#     username        = models.CharField(max_length= 30, unique= True)
#     date_joined     = models.DateTimeField(verbose_name= 'date joined', auto_now_add= True)
#     last_login      = models.DateField(verbose_name= 'last login', auto_now= True)
#     is_admin        = models.BooleanField(default= False)
#     is_active       = models.BooleanField(default= True)
#     is_staff        = models.BooleanField(default= False)
#     is_superuser    = models.BooleanField(default= False)
#     first_name      = models.CharField(verbose_name= 'first name', max_length= 50)
#     last_name       = models.CharField(verbose_name= 'last name', max_length=50)

#     USERNAME_FIELD  = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

#     objects = MyAccountManager()

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj = None):
#         return self.is_admin

#     def has_module_perms(self, app_lable):
#         return True





