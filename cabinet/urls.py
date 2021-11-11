from django.urls import path

from .views import get_user, get_vacancies_of_the_company, get_resume_in_cabinet
from company.views import CreateMyCompany
from resume import views
from vacancy.views import CreateVacancy, EditVacancy

urlpatterns = [
    path('', get_user, name='my_profile'),
    # path('company/', name='users_company'),
    path('company/create/', CreateMyCompany.as_view(), name='create_company'),
    path('vacancies/', get_vacancies_of_the_company, name='vacancies'),
    path('vacancy/create', CreateVacancy.as_view(), name='create_vacancy'),
    path('vacancy/<slug:slug>/edit/', EditVacancy.as_view(),
         name='edit_vacancy'),
    path('resume/', get_resume_in_cabinet, name='users_resume'),
    path('resume/create/', views.create_resume, name='create_resume'),
    path('resume/<int:pk>/edit/', views.EditResume.as_view(),
         name='edit_resume'),
    path('resume/<int:pk>/delete/', views.DeleteResume.as_view(),
         name='delete_resume')


    # path('<slug:slug>/', EditVacancy.as_view(), name='edit_vacancy')

]