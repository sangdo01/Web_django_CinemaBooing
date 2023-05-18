from rest_framework import serializers
from .models import Movie
class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('movie_name', 'content', 'trailer', 'image', 'banner', 'time_of_movie', 'language', 'release_date', 'is_showing', 'status', 'directors', 'actors')

