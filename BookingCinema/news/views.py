from django.shortcuts import render
from .models import News
# import pagination.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def Index(request):
    context = {}
    news = News.objects.filter(status = 1).order_by("-create_at")
    paginator = Paginator(news, 6)
    page_number = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger: 
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context['page_obj'] = page_obj 
    return render(request, 'pages/news.html', context)

def NewsDetail(request, id):
    context = {}
    obj = News.objects.get(id = id)
    news_item = News.objects.filter(status = 1).order_by("-create_at")
    context = {
        'obj': obj,
        'news_item': news_item
    }
    return render(request, 'pages/news_detail.html', context)
