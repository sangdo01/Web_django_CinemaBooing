from django.shortcuts import render
from django.views import View
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')
def contact(request):
    return render(request, 'pages/contact.html')

class HomeView(View):
    def get(self, request):
        return render(request, 'pages/index.html')