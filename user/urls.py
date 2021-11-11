from django.urls import path

from user.views import login_user, register_user, user_logout


urlpatterns = [
   path('login/', login_user, name='login'),
   path('register/', register_user, name='register'),
   path('logout/', user_logout, name='logout'),
]
