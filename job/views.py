from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView


class MainView(TemplateView):
	template_name = 'job/index.html'


class Vacancies(ListView):
	template_name = 'job/vacancies.html'