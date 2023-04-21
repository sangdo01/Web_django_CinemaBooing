from django.contrib import admin
from .models import Movie, Genre, Movie_Actor, Movie_Genre, ReviewRating


class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_name', 'is_showing', 'status']


class Movie_ActorAdmin(admin.ModelAdmin):
    list_display = ['movie', 'actor']


class Movie_GenreAdmin(admin.ModelAdmin):
    list_display = ['movie', 'genre']


class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ['review', 'rate', 'status', 'created_at']
    list_filter = ['status']
    readonly_fields = ('review', 'rate', 'user', 'movie')




# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre)
admin.site.register(Movie_Actor, Movie_ActorAdmin)
admin.site.register(Movie_Genre, Movie_GenreAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)

