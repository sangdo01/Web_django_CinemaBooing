from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from movie.models import Movie
from news.models import News
from django.contrib import messages

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
# Create your views here.




class HomeView(View):
    def get(self, request):
        context = {}
        movies_slider = Movie.objects.filter(status = 1, is_showing =1).order_by("-release_date")[:5]
        movies_now = Movie.objects.filter(status = 1, is_showing =1).order_by("-release_date")      
        movies_comming = Movie.objects.filter(status = 1, is_showing =2).order_by("-release_date")
        news = News.objects.filter(status = 1).order_by("-create_at")
        
        context = {
            'movies_slider': movies_slider,
            'movies_now': movies_now,
            'movies_comming': movies_comming,
            'news': news,
        }
        return render(request, 'pages/index.html', context)
    

def Contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            html = render_to_string('pages/email/contact_form.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            })
            form.save()
            messages.success(request, 'Đánh giá của bạn đã được gửi')
            send_mail(subject, message, email, [settings.EMAIL_HOST], html_message=html)
            return render(request, 'pages/contact.html')
    return render(request, 'pages/contact.html')


def SearchResult(request):
    context = {}
    if request.method == 'POST':
        search = request.POST.get('search', False)
        context['search'] = search
        search_result = Movie.objects.filter(movie_name__contains=search.upper(), status = 1)
        context['search_result'] = search_result
        return render(request, 'pages/search_result.html', context)
    return render(request, 'pages/search_result.html', context)

