from django.db import models
import os
# Create your models here.

class News(models.Model):
    def image_news_upload_to(self, instance = None):
        if(instance):
            return os.path.join("news", instance)
        return None

    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to= image_news_upload_to)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add= True)
    status = models.IntegerField(default= 1)

