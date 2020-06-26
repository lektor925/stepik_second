from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from job.views import MainView, VacanciesAllView, VacanciesCatView, VacancyDetail, CompanyDetail, CompaniesAll, \
    VacancySend, MyCompanyDetail, MyCompanyVacancies, MyCompanyVacancyDetail, UserLogin, UserRegister
from second_project import settings

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('vacancies/', VacanciesAllView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:code>', VacanciesCatView.as_view(), name='vacancies_cat'),
    path('vacancies/<int:pk>', VacancyDetail.as_view(), name='vacancy_detail'),
    path('vacancies/<int:vacancy_id>/send/', VacancySend.as_view(), name='vacancy_send'),
    path('companies/', CompaniesAll.as_view(), name='company_all'),
    path('companies/<int:id>', CompanyDetail.as_view(), name='company_detail'),
    path('mycompany/', MyCompanyDetail.as_view(), name='my_company_detail'),
    path('mycompany/vacancies/', MyCompanyVacancies.as_view(), name='my_company_vacancies'),
    path('mycompany/vacancies/<int:pk>', MyCompanyVacancyDetail.as_view(), name='my_company_vacancy_detail'),
    path('login/', UserLogin.as_view(), name='user_login'),
    path('register/', UserRegister.as_view(), name='user_register'),
    path('logout/', LogoutView.as_view(), name='user_logout'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
