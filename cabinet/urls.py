from django.urls import path

from .views import register_user, login_user, user_logout, my_company, \
   CreateMyCompany, CreateVacancy, get_vacancies_of_the_company, EditVacancy

urlpatterns = [
   path('login/', login_user, name='login'),
   path('register/', register_user, name='register'),
   path('logout/', user_logout, name='logout'),
   path('', my_company, name='my_company'),
   path('create-company/', CreateMyCompany.as_view(), name='create_company'),
   path('vacancies/', get_vacancies_of_the_company, name='vacancies'),
   path('create-vacancy/', CreateVacancy.as_view(), name='create_vacancy'),
   path('<slug:slug>/', EditVacancy.as_view(), name='edit_vacancy')

]