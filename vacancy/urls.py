from django.urls import path

from .views import home_page, Vacancies, VacancyBySpecialization, ViewCompany,\
    ViewVacancy

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('', home_page, name='home_page'),
    path('vacancies/', Vacancies.as_view(), name='vacancies'),
    path('vacancies/<slug:specialization>/', VacancyBySpecialization.as_view(), name='specialization'),
    path('company/<slug:company>/', ViewCompany.as_view(), name='company'),
    path('vacancy/<slug:slug>/', ViewVacancy.as_view(), name='vacancy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)