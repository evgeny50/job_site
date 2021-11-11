from django.urls import path

from .views import create_resume, get_resume, DetailResume, AllResume


urlpatterns = [
    path('', AllResume.as_view(), name='all_resume'),
    path('<int:pk>/', DetailResume.as_view(), name='list_resume'),
    # path('create/', create_resume, name='create_resume'),
    # path('edit/', ),
]