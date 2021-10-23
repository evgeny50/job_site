from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Company, Specialty, Skill, Vacancy, Application


class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    list_display = ('name', 'city', 'employee_count', 'get_photo',)
    fields = (
        'name', 'slug', 'city', 'logo', 'get_photo',
        'description', 'employee_count', 'owner'
    )
    readonly_fields = ('owner', 'get_photo')

    def get_photo(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" width=100>')
        return 'Нет фото'
    get_photo.short_description = 'Фото'


class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'written_username', 'written_phone',
        'written_cover_letter'
    )


class SpecialtyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class VacancyAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'description', 'company', 'specialty',
              'skills', 'salary_min', 'salary_max', 'published_at',
              'created_at', 'contacts'
              )
    readonly_fields = ('update_at', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'company', 'created_at', 'published_at')
    list_editable = ('published_at',)
    list_filter = ('specialty', 'company', 'skills', 'published_at')
    search_fields = ('title', 'company__name', 'description', 'slug')


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Skill)
admin.site.register(Vacancy, VacancyAdmin)
