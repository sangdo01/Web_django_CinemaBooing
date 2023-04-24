from django.urls import path
from .import views

urlpatterns = [
    path('nowshowing/', views.Nowshowing, name='nowshowing'),
    path('nowshowing/<int:id_genre>', views.Nowshowing, name='nowshowing'),
    path('comingsoon/', views.ComingSoon, name='comingsoon'),
    path('comingsoon/<int:id_genre>', views.ComingSoon, name='comingsoon'),
    path('moviedetail/<int:id>', views.MovieDetail, name='moviedetail'),
    path('addreview/<int:id>', views.AddReviewRating, name='addreview'),
    
]