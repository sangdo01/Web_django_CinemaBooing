from django.contrib import admin
from .models import Movie, Movie_Genre, Movie_Actor, Movie_Detail
# Register your models here.
admin.site.register(Movie)
admin.site.register(Movie_Genre)
admin.site.register(Movie_Actor)
admin.site.register(Movie_Detail)