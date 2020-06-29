from django import forms
from django.forms import ModelForm

from job.models import Application, Company


class ApplicationFormVacancyDetail(ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']
        labels = {
            'written_username': 'Вас зовут',
            'written_phone': 'Ваш телефон',
            'written_cover_letter': 'Сопроводительное письмо'
        }


class CompanyForm(ModelForm):
    name = forms.CharField(label='Название компании', widget=forms.widgets.Input(attrs={'class': 'form-control', 'value': 'test'}))

    class Meta:
        model = Company
        fields = ['name', 'location', 'logo', 'description', 'employee_count', 'owner']

