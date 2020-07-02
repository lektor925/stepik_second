from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from job.views import MainView, UserLogin, UserRegister, VacanciesListView, \
    VacanciesCatListView, VacancyDetailView, VacancyDetailSend, CompaniesListView, CompanyDetailView, \
    MyCompanyDetailView, MyCompanyVacanciesListView, my_company_edit, MyCompanyBlankView, \
    MyCompanyVacancyAddView, my_company_vacancy_edit, SearchListView, my_resume_edit, MyResumeAddView
from second_project import settings


if settings.DEBUG:
    urlpatterns = [
        path('', MainView.as_view(), name='home'),
        path('vacancies/', VacanciesListView.as_view(), name='vacancies'),
        path('vacancies/cat/<str:code>', VacanciesCatListView.as_view(), name='vacancies_cat'),
        path('vacancies/<int:pk>', VacancyDetailView.as_view(), name='vacancy_detail'),
        path('vacancies/<int:vacancy_id>/send/', VacancyDetailSend.as_view(), name='vacancy_send'),
        path('companies/', CompaniesListView.as_view(), name='company_all'),
        path('companies/<int:pk>', CompanyDetailView.as_view(), name='company_detail'),
        path('myresume/', my_resume_edit, name='my_resume'),
        path('myresume/add/', MyResumeAddView.as_view(), name='my_resume'),
        path('search/', SearchListView.as_view(), name='search'),
        path('mycompany/', my_company_edit, name='my_company_detail'),
        path('mycompany/blank/', MyCompanyBlankView.as_view(), name='my_company_blank'),
        path('mycompany/add/', MyCompanyDetailView.as_view(), name='my_company_create'),
        path('mycompany/vacancies/', MyCompanyVacanciesListView.as_view(), name='my_company_vacancies'),
        path('mycompany/vacancies/add/', MyCompanyVacancyAddView.as_view(), name='my_company_vacancy_add'),
        path('mycompany/vacancies/<int:pk>/', my_company_vacancy_edit, name='my_company_vacancy_detail'),
        path('login/', UserLogin.as_view(), name='user_login'),
        path('register/', UserRegister.as_view(), name='user_register'),
        path('logout/', LogoutView.as_view(), name='user_logout'),
        path('admin/', admin.site.urls),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
