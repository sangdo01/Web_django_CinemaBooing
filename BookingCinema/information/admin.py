from django.contrib import admin
from .models import Actor, Directors
# Register your models here.

from django.contrib import admin
from .models import Directors, Actor
# Register your models here.

admin.site.register(Directors)
admin.site.register(Actor)