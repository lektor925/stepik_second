from job.models import *

from job.data import *


for item in companies:
	Company.objects.create(name=item['title'])


for item in specialties:
	Specialty.objects.create(code=item['cat'], title=item['title'])


for item in jobs:
	company = Company.objects.get(name=item['company'])
	specialty = Specialty.objects.get(code=item['cat'])
	Vacancy.objects.create(title=item['title'], description=item['desc'], salary_min=item['salary_from'], salary_max=item['salary_to'], published_at=item['posted'], company=company, specialty=specialty)
