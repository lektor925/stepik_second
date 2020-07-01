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

