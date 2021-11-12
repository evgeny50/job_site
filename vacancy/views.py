from django.contrib import messages
from django.http import JsonResponse, Http404
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.views.generic import ListView

from .serializers import VacancySerializer
from .forms import SendCoverLetterForm, SearchForm, HomeSearchForm, \
    FormCreateVacancy
from .servises.servises import (
    get_all_speciality, get_all_company, get_all_vacancies,
    get_vacancy_by_specialization, get_title_specialization, get_company,
    get_vacancy, get_vacancy_contains_query, get_my_company,
    get_vacancy_on_slug
)
from vacancy.models import Vacancy, Application


class CreateVacancy(View):
    """Create a vacancy for the company."""
    template_name = 'cabinet/create_vacancy.html'
    form_class = FormCreateVacancy

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.company_id = get_my_company(request).pk
            form.save()
            messages.success(request, 'Success')
            return redirect('vacancies')
        return render(request, self.template_name, {'form': form})


class EditVacancy(View):
    """Edit and save vacancy."""
    form_class = FormCreateVacancy
    template_name = 'cabinet/create_vacancy.html'

    def get(self, request, slug):
        vacancy = get_vacancy_on_slug(slug)
        application = Application.objects.filter(vacancy__pk=vacancy.pk)
        if not vacancy:
            raise Http404

        form = self.form_class(instance=vacancy)
        context = {
            'form': form,
            'applications': application,
        }
        return render(request, self.template_name, context)

    def post(self, request, slug):
        vacancy = get_vacancy_on_slug(slug)
        form = self.form_class(request.POST, instance=vacancy)
        if not vacancy:
            raise Http404
        if form.is_valid():
            form.save()
            messages.success(request, 'Success')
            return redirect('vacancies')
        return render(request, self.template_name, {'form': form})


def home_page(request):
    query = request.GET.get('q')
    if query:
        return search(request, query=query)
    context = {
        'first_four_speciality': get_all_speciality()[:4],
        'second_four_speciality': get_all_speciality()[4:8],
        'first_four_company': get_all_company()[:4],
        'second_four_company': get_all_company()[4:8],
        'form': HomeSearchForm()
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
    """Displaying vacancies by profession."""
    template_name = 'vacancy/vacancies_by_specialization.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        queryset = get_vacancy_by_specialization(self)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = get_title_specialization(self)
        context['count'] = len(self.get_queryset())
        return context


class ViewCompany(ListView):
    """View all companies."""
    template_name = 'vacancy/company.html'
    context_object_name = 'company'

    def get_queryset(self):
        return get_company(self)


class ViewVacancy(View):
    """Detailed view of the vacancy and sending a response form."""
    form_class = SendCoverLetterForm

    def get(self, request, slug):
        vacancy = get_vacancy(slug)
        form = self.form_class(request.user.pk)
        return render(request, 'vacancy/vacancy.html', {
            'vacancy': vacancy,
            'form': form
        })

    def post(self, request, slug):
        if not request.user.is_authenticated:
            return redirect('login')
        form = self.form_class(request.user.pk, request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.resume = form.cleaned_data['resume']
            form.instance.vacancy = Vacancy.objects.get(slug=slug)
            form.save()
            return render(request, 'vacancy/send.html')


def search(request, query=None):
    form = SearchForm(request.GET or None)
    if not query:
        query = request.GET.get('q')
    if request.method == 'GET':
        if form.is_valid():
            vacancy = get_vacancy_contains_query(query)
            return render(request, 'vacancy/search.html', {
                'form': form,
                'search': query,
                'vacancy': vacancy
            })
    return render(request, 'vacancy/search.html', {'form': form})


def vacancy_api_detail(request, pk):
    if request.method == 'GET':
        vacancy = Vacancy.objects.get(pk=pk, published_at=True)
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data)
