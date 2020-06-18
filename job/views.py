from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class MainView(TemplateView):
	template_name = 'job/index.html'


class VacanciesAllView(TemplateView):
	template_name = 'job/vacancies.html'


class VacanciesCatView(TemplateView):
	template_name = 'job/vacancies_cat.html'


class VacancyDetail(TemplateView):
	template_name = 'job/vacancy_detail.html'


class CompanyDetail(TemplateView):
	template_name = 'job/company_detail.html'
