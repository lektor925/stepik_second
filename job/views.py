from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class MainView(TemplateView):
	template_name = 'job/index.html'


class VacanciesView(TemplateView):
	template_name = 'job/vacancies.html'


class VacanciesCatView(TemplateView):
	template_name = 'job/vacancies_cat.html'
