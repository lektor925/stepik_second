from django import forms
from django.forms import ModelForm

from job.models import Application, Company, Vacancy


class ApplicationFormVacancyDetail(ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']
        labels = {
            'written_username': 'Вас зовут',
            'written_phone': 'Ваш телефон',
            'written_cover_letter': 'Сопроводительное письмо'
        }


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'location', 'logo', 'description', 'employee_count']
        labels = {
            'name': 'Название компании',
            'employee_count': 'Количество человек в компании',
            'location': 'География',
            'logo': 'Логотип',
            'description': 'Информация о компании',
        }
        widgets = {
            'name': forms.widgets.Input(attrs={'class': 'form-control'}),
            'employee_count': forms.widgets.Input(attrs={'class': 'form-control'}),
            'location': forms.widgets.Input(attrs={'class': 'form-control'}),
            'description': forms.widgets.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'logo': forms.widgets.FileInput(attrs={'class': 'custom-file-input'}),
        }


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'specialty', 'skills', 'salary_min', 'salary_max', 'description']
        labels = {
            'title': 'Название вакансии',
            'specialty': 'Специализация',
            'skills': 'Навыки',
            'salary_min': 'Минимальная зарплата',
            'salary_max': 'Максимальная зарплата',
            'description': 'Описание вакансии'
        }
        widgets = {
            'skills': forms.widgets.Textarea(attrs={'rows': 3}),
            'description': forms.widgets.Textarea(attrs={'rows': 5})
        }


class SearchForm(forms.Form):
    s = forms.CharField(max_length=255, widget=forms.widgets.Input(attrs={
        'class': 'form-control w-100',
        'placeholder': 'Найти работу или стажировку',
        'label': 'Поиск'
    }))
