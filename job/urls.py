import debug_toolbar

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vacancy.urls')),
    path('cabinet/', include('cabinet.urls')),
    path('resume/', include('resume.urls')),
    path('account/', include('user.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
