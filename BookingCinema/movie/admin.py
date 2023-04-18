from django.contrib import admin
from .models import Movie, Genre, Movie_Actor, Movie_Genre, ReviewRating



class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ['review', 'rate', 'status', 'created_at']
    list_filter = ['status']
    readonly_fields = ('review', 'rate', 'user', 'movie')




# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Movie_Actor)
admin.site.register(Movie_Genre)
admin.site.register(ReviewRating, ReviewRatingAdmin)

