from django.urls import path
from .import views
from .views import HomeView

urlpatterns = [
    path('home/', views.index),
    path('contact/', views.contact, name='contact'),
    path('', HomeView.as_view(), name='index'),
]

