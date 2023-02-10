from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


# Create your views here.

# def register(request):
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             # user = form.cleaned_data.get('username')
#             # messages.success(request, 'Tài khoản đã được tạo cho ' + user)
#             return redirect('login')
#         # messages.error("Taọ tài khoản không thành công!")
#     form = NewUserForm()

#     context = {'form': form}
#     return render(request, 'pages/register.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Tài khoản ' + user + ' đã được tạo thành công!')
            return redirect('login')
    context = {'form': form}
    return render(request, 'pages/register.html', context)



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
    context = {}
    return render(request, 'pages/login.html', context)


def signout(request):
    pass