from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from job.views import MainView, UserLogin, UserRegister, VacanciesListView, \
    VacanciesCatListView, VacancyDetailView, VacancyDetailSend, CompaniesListView, CompanyDetailView, \
    MyCompanyDetailView, MyCompanyVacanciesListView, MyCompanyVacancyDetailView
from second_project import settings

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:code>', VacanciesCatListView.as_view(), name='vacancies_cat'),
    path('vacancies/<int:pk>', VacancyDetailView.as_view(), name='vacancy_detail'),
    path('vacancies/<int:vacancy_id>/send/', VacancyDetailSend.as_view(), name='vacancy_send'),
    path('companies/', CompaniesListView.as_view(), name='company_all'),
    path('companies/<int:pk>', CompanyDetailView.as_view(), name='company_detail'),
    path('mycompany/', MyCompanyDetailView.as_view(), name='my_company_detail'),
    path('mycompany/vacancies/', MyCompanyVacanciesListView.as_view(), name='my_company_vacancies'),
    path('mycompany/vacancies/<int:pk>', MyCompanyVacancyDetailView.as_view(), name='my_company_vacancy_detail'),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('register/', UserRegister.as_view(), name='user_register'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
