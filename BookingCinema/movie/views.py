from django.shortcuts import render
# import pagination.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Movie, Movie_Genre
# Create your views here.


def MovieDetail(request, pk):
    pass

def Nowshowing(request):
    context = {}
    movies_now = Movie.objects.all().order_by('release_date')
    movie_genre = Movie_Genre.objects.all()
    paginator = Paginator(movies_now, 6)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger: 
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    # page_obj.adjusted_elided_pages = paginator.get_elided_page_range('page')
    # context['movies_now'] = movies_now
    context['movie_genre'] = movie_genre
    context['page_obj'] = page_obj

    return render(request, 'pages/nowshowing.html', context) 




def ComingSoon(request):
    context = {}
    movies_come = Movie.objects.all().order_by('release_date')
    movie_genre = Movie_Genre.objects.all()
    paginator = Paginator(movies_come, 6)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger: 
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context['movies_come'] = movies_come
    context['movie_genre'] = movie_genre
    return render(request, 'pages/comingsoon.html', context) 
