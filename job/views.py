from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from job.forms import ApplicationFormVacancyDetail, CompanyForm
from job.models import Specialty, Company, Vacancy, Application


class MainView(TemplateView):
    template_name = 'job/index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context['specialty'] = Specialty.objects.annotate(Count('vacancies__specialty'))
        context['company'] = Company.objects.annotate(Count('company__company'))
        context['search_list'] = context['specialty'][:4]
        return context


class VacanciesListView(ListView):
    template_name = 'job/vacancies.html'
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super(VacanciesListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Все вакансии'
        context['vacancy_list'] = Vacancy.objects.select_related('company')
        return context


class VacanciesCatListView(ListView):
    template_name = 'job/vacancies.html'
    model = Vacancy
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super(VacanciesCatListView, self).get_context_data(**kwargs)
        context['vacancy_list'] = Vacancy.objects.filter(specialty__code=self.kwargs['code'])\
            .select_related('specialty')\
            .select_related('company')
        context['category_title'] = Specialty.objects.get(code=self.kwargs['code'])
        return context


class VacancyDetailView(DetailView):
    template_name = 'job/vacancy.html'
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super(VacancyDetailView, self).get_context_data(**kwargs)
        context['form'] = ApplicationFormVacancyDetail()
        context['vacancy_id'] = self.kwargs['pk']
        return context


class VacancyDetailSend(TemplateView):
    template_name = 'job/send.html'

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            Application.objects.create(
                written_username=request.POST['written_username'],
                written_phone=request.POST['written_phone'],
                written_cover_letter=request.POST['written_cover_letter'],
                user=request.user,
                vacancy=Vacancy.objects.get(id=self.kwargs['vacancy_id'])
            )
            return redirect(request.path)
        else:
            base_path = request.path.split('/')[:-2]
            new_path = '/'.join(base_path)
            return redirect(new_path)

    def get_context_data(self, **kwargs):
        context = super(VacancyDetailSend, self).get_context_data(**kwargs)
        context['vacancy'] = Vacancy.objects.filter(id=self.kwargs['vacancy_id'])
        return context


class CompaniesListView(ListView):
    model = Company

    def get_context_data(self, **kwargs):
        context = super(CompaniesListView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['company_list'] = Company.objects.filter(owner=self.request.user)
        return context


class CompanyDetailView(DetailView):
    template_name = 'job/company.html'
    model = Company
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['vacancy_list'] = Vacancy.objects.filter(company=self.kwargs['pk'])\
            .select_related('specialty').select_related('company')
        return context


class MyCompanyBlankView(TemplateView):
    template_name = 'job/company-create.html'


class MyCompanyDetailView(CreateView):
    form_class = CompanyForm
    template_name = 'job/company-edit.html'

    def post(self, request, *args, **kwargs):
        form = CompanyForm(request.POST, request.FILES)

        if form.is_valid():
            print(form.cleaned_data)
            Company.objects.create(owner=request.user, **form.cleaned_data)
        return redirect(reverse_lazy('my_company_detail'))


def my_company_edit(request):
    try:
        company = Company.objects.get(owner=request.user)
    except:
        return redirect(reverse_lazy('my_company_blank'))

    if request.method == 'POST':
        company_form = CompanyForm(request.POST, instance=company)
        if company_form.is_valid():
            company_form.save()
            return HttpResponseRedirect(reverse_lazy('my_company_detail'))
        else:
            return render(request, 'job/company-edit.html', {'form': company_form })
    else:
        company_form = CompanyForm(instance=company)
        return render(request, 'job/company-edit.html', {'form': company_form, 'company': company})


class MyCompanyVacanciesListView(TemplateView):
    pass


class MyCompanyVacancyDetailView(TemplateView):
    pass


class UserLogin(LoginView):
    redirect_authenticated_user = False
    template_name = 'job/signup.html'


class UserRegister(CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'job/register.html'
