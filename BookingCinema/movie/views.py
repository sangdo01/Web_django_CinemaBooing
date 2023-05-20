
from audioop import avg
from django.shortcuts import render 
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
# rest framework
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.response import Response  

from django.contrib import messages
from statistics import mean 
# import pagination.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ReviewRatingForm
from .models import Movie, Genre, Directors, ReviewRating
from .serializers import MovieSerializers
# Create your views here.


class NowshowingViewSet(APIView):
    def get(self, request, *args, **kwargs):
        result = Movie.objects.filter(status = 1, is_showing = 1) 
        serializers = MovieSerializers(result, many=True)  
        return Response({'status': 'success', "movies":serializers.data}, status=200)  
    

def Nowshowing(request, id_genre = None):
    context = {}
    movies_now = Movie.objects.filter(status = 1, is_showing = 1)
    movie_genre = Genre.objects.all()
    if id_genre is not None:
        genre = Genre.objects.get(id = id_genre)
        try:
            movies_now = genre.movies.filter(status = 1, is_showing = 1).order_by('-release_date')
        except:
            pass
            
    paginator = Paginator(movies_now, 6)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger: 
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    # page_obj.adjusted_elided_pages = paginator.get_elided_page_range('page')
    context['movie_genre'] = movie_genre
    context['page_obj'] = page_obj

    return render(request, 'pages/nowshowing.html', context) 


def ComingSoon(request, id_genre = None):
    context = {}
    movies_come = Movie.objects.filter(status = 1, is_showing = 2)
    movie_genre = Genre.objects.all()
    if id_genre is not None:
        genre = Genre.objects.get(id = id_genre)
        try:
            movies_come = genre.movies.filter(status = 1, is_showing = 2).order_by('-release_date')
        except:
            pass
    paginator = Paginator(movies_come, 6)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger: 
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context['movie_genre'] = movie_genre
    context['page_obj'] = page_obj
    return render(request, 'pages/comingsoon.html', context) 


def MovieDetail(request, id):
    context = {}
    movie = Movie.objects.get(id = id)
    dicrectors = movie.directors
    actors = movie.actors.through.objects.filter(movie=movie)
    genres = movie.genre_set.all()
    reviews = ReviewRating.objects.filter(movie_id = id).order_by('-created_at')
    qty_star = [1, 2, 3, 4, 5]
    list_rate = []
    for item in reviews:
        list_rate.append(item.rate)
    try:
        avg_rate = round(sum(list_rate) / len(list_rate), 1) 
    except ZeroDivisionError:
        avg_rate = "Chưa có đánh giá"  
    context = {
        'movie': movie,
        'dicrectors': dicrectors,
        'actors': actors,
        'genres': genres,
        'reviews': reviews,
        'qty_star': qty_star,
        'avg_rate': avg_rate,
    }
    return render(request, 'pages/movie_detail.html', context)


def AddReviewRating(request, id):
    url = request.META.get('HTTP_REFERER')
    # return HttpResponse(url)
    if request.method == 'POST':
        form = ReviewRatingForm(request.POST)
        if form.is_valid():
            data = ReviewRating()
            data.review = form.cleaned_data['review']
            data.rate = form.cleaned_data['rate']
            data.movie_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request, 'Đánh giá của bạn đã được gửi')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)



    