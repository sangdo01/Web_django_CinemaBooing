from django.shortcuts import render
from .models import Directors, Actor
# Create your views here.


def AboutUs(request):
    context = {}
    # get list rap chieu
    return render(request, 'pages/about_us.html', context)


def ActorList(request):
    context = {}
    actors = Actor.objects.all()
    context = {
        'actors': actors,
    }
    return render(request, 'pages/actor.html', context)


def DirectorsList(request):
    context = {}
    directors = Directors.objects.all()
    context = {
        'directors': directors,
    }
    return render(request, 'pages/directors.html', context)


def DirectorsDetail(request, id):
    directors = Directors.objects.get(id = id)
    context = {
        'directors': directors,
    }
    return render(request, 'pages/directors_detail.html', context)


def ActorDetail(request, id):
    actor = Actor.objects.get(id = id)
    print(actor)
    context = {
        'actor': actor,
    }
    return render(request, 'pages/actor_detail.html', context)