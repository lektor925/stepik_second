from django import template

register = template.Library()


def myvacancy(value):
    if value % 10 == 0 or value % 10 > 4 or (value % 100 >= 11) and (value % 100 <=15):
        return f'{value} вакансий'
    elif value % 10 == 1:
        return f'{value} вакансия'
    elif (value % 10 > 1) and (value % 10 < 5):
        return f'{value} вакансии'
    else:
        return 'Нет вакансий'


register.filter('myvacancy', myvacancy)
