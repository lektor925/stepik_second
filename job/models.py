from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='companies', blank=True)
    description = models.TextField(blank=True, null=True)
    employee_count = models.IntegerField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company', null=True)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    code = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='vacancies')

    def __str__(self):
        return self.title


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company')
    skills = models.TextField(blank=True, null=True)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']


class Application(models.Model):
    written_username = models.CharField(max_length=62)
    written_phone = models.CharField(max_length=10)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')


class Status(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Grade(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='status')
    salary = models.CharField(max_length=100)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='specialty')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='grade')
    education = models.CharField(max_length=100)
    experience = models.TextField()
    portfolio = models.TextField()
