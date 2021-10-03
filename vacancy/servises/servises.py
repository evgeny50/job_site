from ..models import Vacancy, Company, Specialty

from django.core.exceptions import ObjectDoesNotExist


def get_all_speciality():
    return Specialty.objects.all()


def get_all_company():
    return Company.objects.all()


def get_all_vacancies():
    return Vacancy.objects.all()


def get_vacancy_by_specialization(self):
    return Vacancy.objects.filter(specialty__slug=self.kwargs['specialization'])


def get_title_specialization(self):
    return Specialty.objects.get(slug=self.kwargs['specialization'])


def get_company(self):
    company = Company.objects.get(slug=self.kwargs['company'])
    vacancies = Vacancy.objects.filter(company__slug=company)
    return {
            'company': company,
            'vacancies': vacancies,
            }


def get_vacancy(slug):
    try:
        return Vacancy.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return None


