from django.urls import path

from user import views


urlpatterns = [
   path('', views.EditProfile.as_view(), name='edit_profile'),
   path('login/', views.login_user, name='login'),
   path('login/employer/', views.register_employer, name='login_employer'),
   path('register/', views.register_user, name='register'),
   path('logout/', views.user_logout, name='logout'),
]
