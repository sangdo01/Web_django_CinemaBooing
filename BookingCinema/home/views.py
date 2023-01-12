from django.shortcuts import render
from django.views import View
from movie.models import Movie

# Create your views here.


# def index(request):
#     return render(request, 'pages/index.html')
def contact(request):
    return render(request, 'pages/contact.html')


class HomeView(View):
    def get(self, request):
        movies = Movie.objects.all()
        context = {
            'movies': movies
        }
        return render(request, 'pages/index.html', context)