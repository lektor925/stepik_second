from django.db.models import Count
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from job.models import Specialty, Company, Vacancy


class MainView(TemplateView):
	template_name = 'job/index.html'

	def get_context_data(self, **kwargs):
		context = super(MainView, self).get_context_data(**kwargs)
		context['specialty'] = Specialty.objects.annotate(Count('vacancies__specialty'))
		context['company'] = Company.objects.annotate(Count('company__company'))
		return context


class VacanciesAllView(ListView):
	template_name = 'job/vacancies.html'
	model = Vacancy


class VacanciesCatView(ListView):
	template_name = 'job/vacancies.html'
	model = Vacancy


class VacancyDetail(TemplateView):
	template_name = 'job/vacancy.html'


class CompanyDetail(TemplateView):
	template_name = 'job/company.html'
