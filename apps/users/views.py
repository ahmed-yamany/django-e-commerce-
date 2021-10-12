from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, ProfileEdit
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import User


def register(request):
    context = {}

    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=password)
            login(request, account)
            return redirect('home:home_page')

        else:
            context['form'] = form

    else:
        if request.user.is_authenticated:
            messages.info(request, f'You are already logged in {request.user.username}')
            return redirect('home:home_page')
        else:
            form = RegisterForm()
    return render(request, 'users/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    context = {}

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home:home_page')

    else:
        if request.user.is_authenticated:
            messages.info(request, f'You are already logged in {request.user.username}')
            return redirect('home:home_page')
        else:
            form = LoginForm()

    context['form'] = form

    return render(request, 'users/login.html', context)


def profile(request, username):
    context = {}
    user_profile = User.objects.filter(username=username)

    if request.POST:
        form = ProfileEdit(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.info(request, f'Successfully updated')

            return redirect('profile', username=username)
        else:
            context['form'] = form


    else:
        pass

    if user_profile.exists():
        context['profile'] = user_profile[0]
    return render(request, 'users/profile.html', context)
