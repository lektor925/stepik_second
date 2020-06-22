from django.db.models import Count
from django.shortcuts import render
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
		context['vacancy_list'] = Vacancy.objects.all()
		return context


class VacanciesCatView(ListView):
	template_name = 'job/vacancies.html'
	model = Vacancy

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(VacanciesCatView, self).get_context_data(**kwargs)
		context['category'] = Specialty.objects.get(code=self.kwargs['code'])
		context['vacancy_list'] = Vacancy.objects.filter(specialty__code=self.kwargs['code'])
		return context


class VacancyDetail(DetailView):
	template_name = 'job/vacancy.html'
	model = Vacancy


class CompaniesAll(ListView):
	model = Company


class CompanyDetail(ListView):
	template_name = 'job/company.html'
	model = Vacancy

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super(CompanyDetail, self).get_context_data(**kwargs)
		context['company'] = Company.objects.get(id=self.kwargs['id'])
		context['vacancy_list'] = Vacancy.objects.filter(company_id=self.kwargs['id'])
		return context

