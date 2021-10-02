from django.views import View

from vacancy.models import Vacancy

from django.shortcuts import render, redirect

from .servises.servises import get_all_speciality, get_all_company, \
    get_all_vacancies, get_vacancy_by_specialization, get_title_specialization, \
    get_company, get_vacancy

from .forms import SendCoverLetterForm

from django.views.generic import ListView, DetailView

from django.http import HttpResponseRedirect

from django.http import HttpResponse, JsonResponse
from django.views.decorators import csrf
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import VacancySerializer


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


class ViewVacancy(View):
    form_class = SendCoverLetterForm

    def get(self, request, slug):
        vacancy = get_vacancy(slug)
        form = self.form_class
        return render(request, 'vacancy/vacancy.html', {
            'vacancy': vacancy, 'form': form
        })

    def post(self, request, slug):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.vacancy = Vacancy.objects.get(slug=slug)
            form.save()
            return render(request, 'vacancy/send.html')


def vacancy_api_detail(request, pk):
    if request.method == 'GET':
        vacancy = Vacancy.objects.get(pk=pk, published_at=True)
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data)
