from django.core.exceptions import ObjectDoesNotExist

from resume.models import Resume
from vacancy.models import Company, Vacancy
from vacancy.servises.servises import get_my_company


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
        return ''


def get_resume(request):
    try:
        return Resume.objects.filter(user=request.user.pk)
    except ObjectDoesNotExist:
        return None
