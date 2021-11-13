from django.contrib import admin
from user.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'email')
    list_display_links = ('pk',)


admin.site.register(CustomUser, CustomUserAdmin)
