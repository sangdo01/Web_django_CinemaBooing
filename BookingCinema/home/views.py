from django.shortcuts import render
from django.views import View
from movie.models import Movie
from news.models import News

# Create your views here.


# def index(request):
#     return render(request, 'pages/index.html')
def Contact(request):
    return render(request, 'pages/contact.html')


class HomeView(View):
    def get(self, request):
        context = {}
        movies = Movie.objects.all().order_by("release_date")
        news = News.objects.all().order_by("create_at")
        context['movies'] = movies
        context['news'] = news
        return render(request, 'pages/index.html', context)