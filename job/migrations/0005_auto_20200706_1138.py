# Generated by Django 3.0.7 on 2020-07-06 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job', '0004_auto_20200702_1524'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'Отклик', 'verbose_name_plural': 'Отклики'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Компания', 'verbose_name_plural': 'Компании'},
        ),
        migrations.AlterModelOptions(
            name='grade',
            options={'verbose_name': 'Квалификация', 'verbose_name_plural': 'Квалификации'},
        ),
        migrations.AlterModelOptions(
            name='resume',
            options={'verbose_name': 'Резюме', 'verbose_name_plural': 'Резюме'},
        ),
        migrations.AlterModelOptions(
            name='specialty',
            options={'verbose_name': 'Специализация', 'verbose_name_plural': 'Специализации'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус поиска', 'verbose_name_plural': 'Статусы поиска'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['-published_at'], 'verbose_name': 'Вакансия', 'verbose_name_plural': 'Вакансии'},
        ),
        migrations.AlterField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='applications',
                                    to=settings.AUTH_USER_MODEL,
                                    verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='application',
            name='vacancy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='applications',
                                    to='job.Vacancy',
                                    verbose_name='Вакансия'),
        ),
        migrations.AlterField(
            model_name='application',
            name='written_cover_letter',
            field=models.TextField(verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='application',
            name='written_phone',
            field=models.CharField(max_length=10, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='application',
            name='written_username',
            field=models.CharField(max_length=62, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='company',
            name='employee_count',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество сотрудников'),
        ),
        migrations.AlterField(
            model_name='company',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, upload_to='companies', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='company',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='company',
                                    to=settings.AUTH_USER_MODEL,
                                    verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='education',
            field=models.CharField(max_length=100, verbose_name='Образование'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='experience',
            field=models.TextField(verbose_name='Опыт работы'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='grade', to='job.Grade',
                                    verbose_name='Квалификация'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='portfolio',
            field=models.TextField(verbose_name='Портфолио'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='salary',
            field=models.CharField(max_length=100, verbose_name='Зарплата'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='specialty', to='job.Specialty',
                                    verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='status', to='job.Status',
                                    verbose_name='Статус поиска'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='surname',
            field=models.CharField(max_length=64, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='user', to=settings.AUTH_USER_MODEL,
                                    verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='code',
            field=models.CharField(max_length=100, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='picture',
            field=models.ImageField(upload_to='vacancies', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='status',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='company', to='job.Company',
                                    verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_max',
            field=models.IntegerField(verbose_name='Максимальная зарплата'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_min',
            field=models.IntegerField(verbose_name='Минимальная зарплата'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='skills',
            field=models.TextField(blank=True, null=True, verbose_name='Навыки'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='vacancies', to='job.Specialty',
                                    verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
