from django.contrib import admin
from .models import Movie, Genre, Movie_Actor, Movie_Genre
# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Movie_Actor)
admin.site.register(Movie_Genre)

