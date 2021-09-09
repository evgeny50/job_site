from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.views.generic import View

from django.contrib.auth import login, logout

from .forms import FormRegisterUser, FormLoginUser, FormCreateCompany, \
    FormCreateVacancy
from .servises.servises import get_my_company, get_vacancies
from django.contrib import messages


def register_user(request):
    """Create user"""
    if request.method == 'POST':
        form = FormRegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('vacancies')
    else:
        form = FormRegisterUser()
    return render(request, 'cabinet/register.html',
                  {'form': form, 'title': 'Create account'})


def login_user(request):
    """Authentication user"""
    if request.method == 'POST':
        form = FormLoginUser(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('vacancies')
    else:
        form = FormLoginUser()
    return render(request, 'cabinet/login.html',
                  {'form': form, 'title': 'Login'})


def user_logout(request):
    logout(request)
    return redirect('login')


def my_company(request):
    """Getting a company that is
    tied to a user, if it exists"""
    company = get_my_company(request)
    if company:
        return redirect('create_company')
    return render(request, 'cabinet/company-create.html', {'company': company})


def get_vacancies_of_the_company(request):
    """Getting vacancies of the company, if it exists"""
    vacancies = get_vacancies(request)
    if vacancies:
        return render(request, 'cabinet/vacancy-list.html', {'vacancies': vacancies})
    return render(request, 'cabinet/company-create.html', {'vacancies': vacancies})


class CreateMyCompany(LoginRequiredMixin, View):
    """Creating a company from form"""
    form_class = FormCreateCompany
    template_name = 'cabinet/company-edit.html'

    def get(self, request):
        company = get_my_company(request)
        if not company:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})
        form = self.form_class(instance=company)
        return render(request, self.template_name, {
            'form': form,
            'logo': company.logo
        })

    def post(self, request):
        company = get_my_company(request)
        if company:
            form = self.form_class(request.POST, request.FILES,
                                   instance=company)
        else:
            form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            messages.success(request, 'Отлично')
            return redirect('create_company')
        return render(request, self.template_name, {'form': form})


class CreateVacancy(View):
    """Create a vacancy for the company"""
    template_name = 'cabinet/create_vacancy.html'
    form_class = FormCreateVacancy

    def get(self, request):
        vacancies = get_vacancies(request)
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        pass