from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from . import forms
from .services.services import get_user


def register_user(request):
    """Create user."""
    if request.method == 'POST':
        form = forms.FormRegisterUser(request.POST)
        if form.is_valid():
            form.instance.is_aspirant = True
            user = form.save()
            user.groups.add(Group.objects.get(name='aspirant'))
            login(request, user)
            return redirect('vacancies')
    else:
        form = forms.FormRegisterUser()
    context = {
        'form': form,
        'title': 'Create account'
    }
    return render(request, 'user/register.html', context)


def register_employer(request):
    """Create employer."""
    if request.method == 'POST':
        form = forms.FormRegisterEmployer(request.POST)
        if form.is_valid():
            form.instance.is_employer = True
            user = form.save()
            user.groups.add(Group.objects.get(name='emploer'))
            login(request, user)
            return redirect('vacancies')
    else:
        form = forms.FormRegisterEmployer()
    context = {
        'form': form,
        'title': 'Create account'
    }
    return render(request, 'user/register-employer.html', context)


def login_user(request):
    """Authentication user."""
    if request.method == 'POST':
        form = forms.FormLoginUser(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('my_profile')
    else:
        form = forms.FormLoginUser()
    context = {
        'form': form,
        'title': 'Login'
    }
    return render(request, 'user/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')


class EditProfile(View):
    form = forms.FormEditProfile
    template_name = 'user/edit-profile.html'

    def get(self, request):
        user = get_user(request)
        if user:
            form = self.form(instance=user)
            return render(request, self.template_name, {'form': form})

    def post(self, request):
        user = get_user(request)
        form = self.form(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'inf')
        return render(request, self.template_name, {'form': form})
