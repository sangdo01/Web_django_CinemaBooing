
from audioop import avg
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
# import pagination.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ReviewRatingForm
from .models import Movie, Genre, Directors, ReviewRating
from django.contrib import messages
from statistics import mean 
# Create your views here.


def Nowshowing(request):
    context = {}
    # movies_now = Movie.objects.all().order_by('release_date')
    movies_now = Movie.objects.filter(status = 1, is_showing = 1)
    movie_genre = Genre.objects.all()
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
    # movies_come = Movie.objects.all().order_by('release_date')
    movies_come = Movie.objects.filter(status = 1, is_showing = 2)
    movie_genre = Genre.objects.all()
    paginator = Paginator(movies_come, 6)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger: 
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    # context['movies_come'] = movies_come
    context['movie_genre'] = movie_genre
    context['page_obj'] = page_obj
    return render(request, 'pages/comingsoon.html', context) 


def MovieDetail(request, id):
    context = {}
    movie = Movie.objects.get(id = id)
    reviews = ReviewRating.objects.filter(movie_id = id).order_by('-created_at')
    qty_star = [1, 2, 3, 4, 5]
    list_rate = []
    for item in reviews:
        list_rate.append(item.rate)
    avg_rate =round(sum(list_rate) / len(list_rate), 1) 
    context = {
        'movie': movie,
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
    