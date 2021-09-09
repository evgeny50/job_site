import vacancy.models

from django.shortcuts import render

from .servises.servises import get_all_speciality, get_all_company, \
    get_all_vacancies, get_vacancy_by_specialization, get_title_specialization,\
    get_company

from django.views.generic import ListView, DetailView


def home_page(request):
    context = {
        'first_four_speciality': get_all_speciality()[:4],
        'second_four_speciality': get_all_speciality()[4:8],
        'first_four_company': get_all_company()[:4],
        'second_four_company': get_all_company()[4:8]
    }
    return render(request, 'index.html', context)


class Vacancies(ListView):
    template_name = 'vacancy/vacancies.html'
    context_object_name = 'vacancies'
    paginate_by = 4

    def get_queryset(self):
        return get_all_vacancies()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = len(self.get_queryset())
        return context


class VacancyBySpecialization(ListView):
    template_name = 'vacancy/vacancies_by_specialization.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        global queryset
        queryset = get_vacancy_by_specialization(self)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = get_title_specialization(self)
        context['count'] = len(queryset)
        return context


class ViewCompany(ListView):
    template_name = 'vacancy/company.html'
    context_object_name = 'company'

    def get_queryset(self):
        return get_company(self)


class ViewVacancy(DetailView):
    model = vacancy.models.Vacancy
    template_name = 'vacancy/vacancy.html'
    context_object_name = 'vacancy'



