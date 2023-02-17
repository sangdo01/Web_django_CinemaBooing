from django.urls import path
from .import views
# from .views import 

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name= 'logout'),
    # path('', HomeView.as_view(), name='index'),
]
