from django.urls import path
from .import views

urlpatterns = [
    path('about/', views.AboutUs, name='about'),
    path('directors_detail/<int:id>', views.DirectorsDetail, name='directors_detail'),
    path('actor_detail/<int:id>', views.ActorDetail, name='actor_detail'),
]