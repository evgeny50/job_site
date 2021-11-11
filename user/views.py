from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import FormRegisterUser, FormLoginUser


def register_user(request):
    """Create user."""
    if request.method == 'POST':
        form = FormRegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('vacancies')
    else:
        form = FormRegisterUser()
    context = {
        'form': form,
        'title': 'Create account'
    }
    return render(request, 'user/register.html', context)


def login_user(request):
    """Authentication user."""
    if request.method == 'POST':
        form = FormLoginUser(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('my_profile')
    else:
        form = FormLoginUser()
    context = {
        'form': form,
        'title': 'Login'
    }
    return render(request, 'user/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')
