from django.urls import path
from .import views

urlpatterns = [
    path('nowshowing/', views.Nowshowing, name='nowshowing'),
    path('comingsoon/', views.ComingSoon, name='comingsoon'),
]