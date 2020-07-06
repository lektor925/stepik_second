from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    location = models.CharField(max_length=255, blank=True, null=True, verbose_name='Город')
    logo = models.ImageField(upload_to='companies', blank=True, verbose_name='Логотип')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    employee_count = models.IntegerField(blank=True, null=True, verbose_name='Количество сотрудников')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='company',
                              null=True,
                              verbose_name='Владелец')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Specialty(models.Model):
    code = models.CharField(max_length=100, verbose_name='Код')
    title = models.CharField(max_length=255, verbose_name='Название')
    picture = models.ImageField(upload_to='vacancies', verbose_name='Изображение')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'


class Vacancy(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    specialty = models.ForeignKey(Specialty,
                                  on_delete=models.CASCADE,
                                  related_name='vacancies',
                                  verbose_name='Специализация')
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                related_name='company',
                                verbose_name='Компания')
    skills = models.TextField(blank=True, null=True, verbose_name='Навыки')
    description = models.TextField(verbose_name='Описание')
    salary_min = models.IntegerField(verbose_name='Минимальная зарплата')
    salary_max = models.IntegerField(verbose_name='Максимальная зарплата')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'


class Application(models.Model):
    written_username = models.CharField(max_length=62, verbose_name='Имя')
    written_phone = models.CharField(max_length=10, verbose_name='Телефон')
    written_cover_letter = models.TextField(verbose_name='Сообщение')
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications', verbose_name='Вакансия')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'


class Status(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус поиска'
        verbose_name_plural = 'Статусы поиска'


class Grade(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Квалификация'
        verbose_name_plural = 'Квалификации'


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name='Пользователь')
    name = models.CharField(max_length=64, verbose_name='Имя')
    surname = models.CharField(max_length=64, verbose_name='Фамилия')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status', verbose_name='Статус поиска')
    salary = models.CharField(max_length=100, verbose_name='Зарплата')
    specialty = models.ForeignKey(Specialty,
                                  on_delete=models.CASCADE,
                                  related_name='specialty',
                                  verbose_name='Специализация')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='grade', verbose_name='Квалификация')
    education = models.CharField(max_length=100, verbose_name='Образование')
    experience = models.TextField(verbose_name='Опыт работы')
    portfolio = models.TextField(verbose_name='Портфолио')

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'
