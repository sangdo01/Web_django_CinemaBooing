from django.shortcuts import render

# Create your views here.

def AboutUs(request):
    context = {}
    return render(request, 'pages/about_us.html', context)