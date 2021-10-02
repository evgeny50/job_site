import django.db

from vacancy.models import Company, Vacancy

from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist


def get_my_company(request):
    try:
        company = Company.objects.get(owner=request.user)
        return company
    except ObjectDoesNotExist:
        return None


def get_vacancies(request):
    try:
        vacancies = Vacancy.objects.filter(
            company_id=get_my_company(request).pk
        )
    except AttributeError:
        return None
    return vacancies


def get_name_company(form):
    if len(Company.objects.filter(name=form['name'])) > 0:
        return 'Такая компания уже сущ'


def get_vacancy_on_slug(slug):
    try:
        vacancy = Vacancy.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return None
    return vacancy
