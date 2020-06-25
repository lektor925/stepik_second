from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from job.forms import ApplicationFormVacancyDetail
from job.models import Specialty, Company, Vacancy


class MainView(TemplateView):
    template_name = 'job/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['specialty'] = Specialty.objects.annotate(Count('vacancies__specialty'))
        context['company'] = Company.objects.annotate(Count('company__company'))
        context['search_list'] = context['specialty'][:4]
        return context


class VacanciesAllView(ListView):
    template_name = 'job/vacancies.html'
    model = Vacancy

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(VacanciesAllView, self).get_context_data(**kwargs)
        context['page_title'] = 'Все вакансии'
        context['vacancy_list'] = Vacancy.objects.all()
        return context


class VacanciesCatView(ListView):
    template_name = 'job/vacancies.html'
    model = Vacancy
    allow_empty = False

    def get_queryset(self):
        return Vacancy.objects.filter(specialty__code=self.kwargs['code'])


class VacancyDetail(DetailView):
    template_name = 'job/vacancy.html'
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super(VacancyDetail, self).get_context_data(**kwargs)
        context['form'] = ApplicationFormVacancyDetail()
        context['vacansy_id'] = self.kwargs['pk']
        return context


class VacancySend(TemplateView):
    template_name = 'job/send.html'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(self.kwargs['vacansy_id'])
        return redirect('/')


class CompaniesAll(ListView):
    model = Company


class CompanyDetail(ListView):
    template_name = 'job/company.html'
    model = Vacancy
    allow_empty = False

    def get_queryset(self):
        return Vacancy.objects.filter(company_id=self.kwargs['id'])


class MyCompanyDetail(TemplateView):
    pass


class MyCompanyVacancies(TemplateView):
    pass


class MyCompanyVacancyDetail(TemplateView):
    pass


class UserLogin(LoginView):
    redirect_authenticated_user = False
    template_name = 'job/signup.html'


class UserRegister(CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'job/register.html'
