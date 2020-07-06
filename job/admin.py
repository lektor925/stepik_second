from django.contrib import admin

from job.models import Company, Specialty, Vacancy, Application, Status, Grade, Resume


class CompanyAdmin(admin.ModelAdmin):
    pass


class SpecialtyAdmin(admin.ModelAdmin):
    pass


class VacancyAdmin(admin.ModelAdmin):
    pass


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'written_username', 'written_phone', 'vacancy', 'user']
    list_display_links = ('id', 'written_username')
    list_filter = ('vacancy', 'user')
    list_per_page = 20


class StatusAdmin(admin.ModelAdmin):
    pass


class GradeAdmin(admin.ModelAdmin):
    pass


class ResumeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Resume, ResumeAdmin)
