
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .servises.servises import get_vacancies, get_resume
from vacancy.servises.servises import get_my_company

# from resume.views import menu_resume


def get_user(request):
    if request.user.is_superuser:
        return my_company(request)
    return get_resume_in_cabinet(request)


def my_company(request):
    """Getting a company that is tied to a user, if it exists."""
    company = get_my_company(request)
    if company:
        return redirect('create_company')
    context = {'company': company}
    return render(request, 'cabinet/company-create.html', context)


def listing(request):
    if request.user.is_superuser:
        vacancies = get_vacancies(request)
        paginator = Paginator(vacancies, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return page_obj
    resume = get_resume(request)
    paginator = Paginator(resume, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def get_vacancies_of_the_company(request):
    """Getting vacancies of the company, if it exists."""
    vacancies = get_vacancies(request)
    context = {
        'vacancies': vacancies
    }
    if vacancies:
        context['page_obj'] = listing(request)
        return render(request, 'cabinet/vacancy-list.html', context)
    return render(request, 'cabinet/company-create.html', context)


def get_resume_in_cabinet(request):
    resume = get_resume(request)
    context = {
        'resume': resume
    }
    if resume:
        context['page_obj'] = listing(request)
        return render(request, 'resume/list-resume.html', context)
    return render(request, 'cabinet/company-create.html', context)




