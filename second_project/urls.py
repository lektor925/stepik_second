from django.contrib import admin
from django.urls import path

from job.views import MainView, VacanciesAllView, VacanciesCatView, VacancyDetail, CompanyDetail

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('vacancies/', VacanciesAllView.as_view(), name='vacancies'),
    path('vacancies/cat/<int:id>', VacanciesCatView.as_view(), name='vacancies_cat'),
    path('vacancies/<int:pk>', VacancyDetail.as_view(), name='vacancy_detail'),
    path('companies/<int:id>', CompanyDetail.as_view(), name='company_detail'),
    path('admin/', admin.site.urls),
]
