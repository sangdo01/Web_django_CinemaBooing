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
        movies_slider = Movie.objects.filter(status = 1, is_showing =1).order_by("-release_date")[:5]
        movies_now = Movie.objects.filter(status = 1, is_showing =1).order_by("-release_date")      
        movies_comming = Movie.objects.filter(status = 1, is_showing =2).order_by("-release_date")
        news = News.objects.filter(status = 1).order_by("-create_at")
        # print(list_cate)
        context = {
            'movies_slider': movies_slider,
            'movies_now': movies_now,
            'movies_comming': movies_comming,
            'news': news,
        }
        return render(request, 'pages/index.html', context)