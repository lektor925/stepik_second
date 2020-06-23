from django.db.models import Count
from django.views.generic import TemplateView, ListView, DetailView

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


class CompaniesAll(ListView):
    model = Company


class CompanyDetail(ListView):
    template_name = 'job/company.html'
    model = Vacancy
    allow_empty = False

    def get_queryset(self):
        return Vacancy.objects.filter(company_id=self.kwargs['id'])
