from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from job.models import Specialty, Company


class MainView(TemplateView):
	template_name = 'job/index.html'

	def get_context_data(self, **kwargs):
		context = super(MainView, self).get_context_data(**kwargs)
		context['specialty'] = Specialty.objects.all()
		context['company'] = Company.objects.all()
		return context


class VacanciesAllView(TemplateView):
	template_name = 'job/vacancies.html'


class VacanciesCatView(TemplateView):
	template_name = 'job/vacancies.html'


class VacancyDetail(TemplateView):
	template_name = 'job/vacancy.html'


class CompanyDetail(TemplateView):
	template_name = 'job/company.html'
