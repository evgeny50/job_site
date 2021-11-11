from django.contrib import admin

from .models import Grade, Resume, Status, Specialty


class ResumeAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('pk', 'first_name', 'specialty', 'grade')
    list_display_links = ('pk',)
    readonly_fields = ('user',)


class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('title',)


class GradeAdmin(admin.ModelAdmin):
    list_display = ('title',)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Resume, ResumeAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Specialty, SpecialtyAdmin)