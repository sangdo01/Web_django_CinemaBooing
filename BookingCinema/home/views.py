from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from movie.models import Movie
from news.models import News
from django.contrib import messages

from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.




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
            send_mail("The contact form subject", "This is message", "dvs@gmail.com", ['example@gmail.com'], html_message=html)
            return render(request, 'pages/contact.html')
    return render(request, 'pages/contact.html')