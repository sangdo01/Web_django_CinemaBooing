from django.urls import path
from .import views

urlpatterns = [
    path('', views.Index, name='news'),
    path('NewsDetail/<int:id>/', views.NewsDetail, name='news-detail'),
]