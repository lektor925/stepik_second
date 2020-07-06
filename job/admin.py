from django.contrib import admin

from job.models import Company, Specialty, Vacancy, Application, Status, Grade, Resume


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'employee_count', 'owner']
    list_display_links = ('id', 'name')
    list_per_page = 20


class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'code']
    list_display_links = ('id', 'title')
    list_per_page = 20


class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'specialty', 'company', 'salary_min', 'salary_max', 'published_at']
    list_display_links = ('id', 'title')
    list_filter = ('specialty', 'company')
    list_per_page = 20


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'written_username', 'written_phone', 'vacancy', 'user']
    list_display_links = ('id', 'written_username')
    list_filter = ('vacancy', 'user')
    list_per_page = 20


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ('id', 'title')


class GradeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ('id', 'title')


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'status', 'salary', 'specialty', 'grade', 'education']
    list_display_links = ('id', 'user')
    list_filter = ('status', 'specialty', 'grade', 'education')
    list_per_page = 20


admin.site.register(Company, CompanyAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Resume, ResumeAdmin)
