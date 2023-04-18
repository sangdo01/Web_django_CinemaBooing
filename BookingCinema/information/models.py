from django.db import models
import os
# Create your models here.
class Actor(models.Model):
    def image_upload_to(self, instance = None):
        if instance:
            return os.path.join("info/actor", instance)
        return None

    actor_name = models.CharField(max_length=255)
    date = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(default= 'default/user.png',upload_to= image_upload_to, max_length=255, null= True, blank=True)
    description = models.TextField(null= True, blank=True)

    def __str__(self):
        return self.actor_name
        


class Directors(models.Model):
    def image_upload_to(self, instance = None):
        if instance:
            return os.path.join("info/directors", instance)
        return None

    directors_name = models.CharField(max_length=255)
    year_of_birth = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(default= 'default/user.png', upload_to= image_upload_to, max_length=500, null= True, blank=True)
    descripton = models.TextField(null= True, blank=True)

    def __str__(self):
        return self.directors_name
        


